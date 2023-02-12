"""
Implementacje algorytmów K-random oraz closest-neighbour
rozwiązujące problem komiwojażera
"""

import tsplib95
import random

mini = 10000
instance = tsplib95.load('berlin52.tsp')
cities = list(instance.get_nodes())
cities_len = len(cities)

#aktualna trasa minimalizująca odległości pomiędzy miastami
tour = [0 for j in range(int(cities_len))]
for i in range(0, int(cities_len)):
    tour[i] = i
random.shuffle(tour)

best_tour = tour.copy()

#macierz przechowująca odległości pomiędzy miastami
matr = [[0 for _ in range(cities_len)] for _ in range(cities_len)]


"""
Funkcja wypełniająca macierz wartościami z danej instancji tsp
"""
def fill_matrix(l):
    for i in range(0, cities_len):
        for j in range(0, cities_len):
            edge = i + l, j + l
            global matr
            matr[i][j] = instance.get_weight(*edge)


"""
Funkcja obliczająca długość drogi na aktualnej trasie
"""
def destination(tour_tmp):
    weight = 0
    for i in range(0, int(cities_len) - 1):
        weight += matr[tour_tmp[i]][tour_tmp[i + 1]]

    weight += matr[tour_tmp[int(cities_len) - 1]][tour_tmp[0]]
    return weight


def get_result_closest_neighbour():
    global best_tour
    best_tour[0] = random.randint(0, cities_len - 1)  # wrzuc losowe miasto na poczatek
    global tour
    tour.remove(best_tour[0])  # usun z wyjsciowej tablicy miasto

    print("\nNajlepsza znaleziona trasa: ", closest_neighbour())
    tour = best_tour.copy()
    print("Długość trasy: ", destination(tour))


"""
Algorytm najbliższego sąsiada (closest neighbour), który jako kolejny wierzchołek wybiera
najlbliższego sąsiada aktualnego wierzchołka
"""
def closest_neighbour():
    for i in range(0, int(cities_len) - 1):
        global best_tour
        global tour
        cls = matr[best_tour[i]][tour[0]]
        best_tour[i+1] = tour[0]
        if len(tour) > 1:
            for j in range(1, len(tour)):
                if matr[best_tour[i]][tour[j]] < cls:
                    cls = matr[best_tour[i]][tour[j]]
                    best_tour[i + 1] = tour[j]               #j jest najblizszym sasaidem
            tour.remove(best_tour[i+1])

        else:
            best_tour[i+1] = tour[0]
    return best_tour




def extended_closest_neighbour(optTour, tour):
    for i in range(0, int(cities_len) - 1):
        cls = matr[optTour[i]][tour[0]]
        optTour[i + 1] = tour[0]
        if len(tour) > 1:
            for j in range(1, len(tour)):
                if matr[optTour[i]][tour[j]] < cls:
                    cls = matr[optTour[i]][tour[j]]
                    optTour[i + 1] = tour[j]
            tour.remove(optTour[i + 1])

        else:
            optTour[i + 1] = tour[0]
    return optTour



"""
Implementacja algorytmu K-random, który polega na wygenerowaniu dopuszczalnego
losowego rozwiązania wiele razy i wybraniu najlepszego z nich wszystkich.
"""
def k_random():
    for i in range(0, 100000):
        global tour
        random.shuffle(tour)
        weight = destination(tour)
        global mini
        global best_tour
        if weight < mini:
            mini = weight
            best_tour = tour.copy()


def get_result_k_random():
    global mini
    mini = destination(tour)
    k_random()
    print("Najlepsza znaleziona trasa: ", best_tour)
    print("Długość trasy: ", mini)



"""
Pomocnicza funkcja zamianiająca miasta kolejnością
"""
def opt_swap_2(swap_tour, i, j):
    swap_tour[i], swap_tour[j] = swap_tour[j], swap_tour[i]
    dest_tmp = destination(swap_tour)
    swap_tour[i], swap_tour[j] = swap_tour[j], swap_tour[i]
    return dest_tmp


def opt_swap(swap_tour, i, j):
    swap_tour[i], swap_tour[j] = swap_tour[j], swap_tour[i]
    return swap_tour

"""
Implementacja algorytmu opt2, polegającego na usuwaniu krzyżowań pomiędzy miastami
w celu minimalizacji długości trasy.
"""
def opt2(acutal_tour):
    potential_tour = acutal_tour.copy()

    mini = opt_swap_2(acutal_tour, 0, 1)
    k,l = 0,1

    for i in range(0, len(acutal_tour)):
        for j in range(i + 1, len(acutal_tour)):
            potential_mini = opt_swap_2(acutal_tour, i, j)
            if potential_mini < mini:
                mini = potential_mini
                k,l = i, j

    if mini < destination(potential_tour):
        opt2(opt_swap(acutal_tour, k, l))
    else:
        print("\nNajlepsza znaleziona trasa: ", potential_tour)
        print("Długość najlepszej znalezionej trasy: ", destination(potential_tour))


"""
Algorytm jako trasy początkowej wykorzystuje trasę zwróconą przez rozszerzony
algorytm najbliższego sąsiada, a następnie wywołuje funkcję opt2
"""
def get_result_opt2(tour):
    droga = get_result_extended_closest_neighbour(True)
    print("Trasa przed: ", droga)
    print("Długość trasy przed: ", destination(droga))
    opt2(droga)


def get_result_extended_closest_neighbour(is2opt):
    tour_copy = tour.copy()
    best_tour[0] = tour[0]
    tour_copy.remove(tour[0])
    random.shuffle(tour_copy)

    extended_closest_neighbour(best_tour, tour_copy)
    mini2 = destination(best_tour)
    droga = best_tour

    for i in range(1, int(cities_len)):
        tour_copy = tour.copy()
        best_tour[0] = tour[i]
        tour_copy.remove(best_tour[0])
        random.shuffle(tour_copy)
        extended_closest_neighbour(best_tour, tour_copy)
        if destination(best_tour) < mini2:
            droga = best_tour.copy()
            mini2 = destination(best_tour)

    if not is2opt:
        print("\nNajlepsza znaleziona trasa: ", droga)
        print("Długość najlepszej znalezionej trasy: ", destination(droga))
    return droga


def main():
    if not instance.is_full_matrix() and not instance.is_explicit():
        fill_matrix(1)
    else:
        fill_matrix(0)

    print("Wybierz algorytm do rowiązania problemu komiwojażera:")
    print("1) K_random")
    print("2) Algorytm najbliższego sąsiada")
    print("3) 2-OPT")
    print("4) Rozszerzony algorytm najbliższego sąsiada")
    algo_nr = input("Twój wybór: ")

    if algo_nr == '1':
        get_result_k_random()
    elif algo_nr == '2':
        get_result_closest_neighbour()
    elif algo_nr == '3':
        get_result_opt2(tour)
    elif algo_nr == '4':
        get_result_extended_closest_neighbour(False)


if __name__ == "__main__":
    main()
