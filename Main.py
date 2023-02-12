import random
import time
import tsplib95
from algorithms import opt_swap
from algorithms import opt_swap_2
from algorithms import extended_closest_neighbour
from algorithms import fill_matrix
from algorithms import destination

instance = tsplib95.load('berlin52.tsp')
cities = list(instance.get_nodes())
cities_len = len(cities)
sumA = sumB = sumC = 0
time1 = time2 = time3 = time4 = 0
end = 10
licznik = 0
il = 5

# losowa macierz odległości
matr2 = [[0 for _ in range(il)] for _ in range(il)]
for i in range(il):
    for j in range(il):
        matr2[i][j] = random.randint(1, 1000)

sumA = sumB = sumC = 0
time1 = time2 = time3 = time4 = 0

tour = [0 for j in range(int(cities_len))]
optTour = [0 for j in range(int(cities_len))]
matr = [[0 for _ in range(cities_len)] for _ in range(cities_len)]


def opt2(acutal_tour):
    potential_tour = acutal_tour.copy()

    mini = opt_swap_2(acutal_tour, 0, 1)
    k, l = 0, 1

    global a4
    a4 = time.time()
    for i in range(0, len(acutal_tour)):
        for j in range(i + 1, len(acutal_tour)):
            potential_mini = opt_swap_2(acutal_tour, i, j)
            if potential_mini < mini:
                mini = potential_mini
                k = i
                l = j
    global b4
    b4 = time.time()
    global licznik
    licznik += 1
    global time4
    time4 += ((b4 - a4) * 1000)
    if (mini < destination(potential_tour)):
        opt2(opt_swap(acutal_tour, k, l))
    else:
        global sumC
        sumC += destination(potential_tour)


def result(tour):
    tour_copy = tour.copy()
    tour_copy_2 = tour.copy()
    random.shuffle(tour_copy_2)
    optTour[0] = tour_copy_2[0]
    tour_copy_2.remove(tour_copy_2[0])
    global a1
    a1 = time.time()
    extended_closest_neighbour(optTour, tour_copy_2)
    global b1
    b1 = time.time()
    global time1
    time1 += ((b1 - a1) * 1000)
    destination(optTour)
    global sumA
    sumA += destination(optTour)

    global a2
    a2 = time.time()
    optTour[0] = tour[0]
    tour_copy.remove(tour[0])
    random.shuffle(tour_copy)
    extended_closest_neighbour(optTour, tour_copy)
    mini2 = destination(optTour)

    droga = optTour
    for i in range(1, int(cities_len)):
        tour_copy = tour.copy()
        optTour[0] = tour[i]
        tour_copy.remove(optTour[0])
        random.shuffle(tour_copy)
        extended_closest_neighbour(optTour, tour_copy)
        if destination(optTour) < mini2:
            droga = optTour.copy()
            mini2 = destination(optTour)
    global b2
    b2 = time.time()
    global time2
    time2 += ((b2 - a2) * 1000)

    global sumB
    sumB += destination(droga)

    global a3
    a3 = time.time()
    opt2(droga)
    global b3
    b3 = time.time()
    global time3
    time3 += ((b3 - a3) * 1000)


def main():
    global sumA, sumB, sumC, sumD, time1, time2, time3, time4
    for i in range(0, end):
        for i in range(0, int(cities_len)):
            tour[i] = i
        random.shuffle(tour)

        if not instance.is_full_matrix() and not instance.is_explicit():
            fill_matrix(1)
        else:
            fill_matrix(0)

        result(tour)

    print("Wyniki dla podanej macierzy odległości")
    print('sumA: ', sumA / end)
    print('sumB: ', sumB / end)
    print('sumC: ', sumC / end)
    print('')

    print('timeA: ', time1 / end)
    print('timeB: ', time2 / end)
    print('timeC: ', time3 / end)
    print('timeD: ', time4 / end)

    random.shuffle(tour)
    global matr
    matr = matr2.copy()
    print("\n\nWyniki dla losowej macierzy odległości")

    sumA = sumB = sumC = 0
    time1 = time2 = time3 = time4 = 0

    result(tour)

    print('sumA: ', sumA / end)
    print('sumB: ', sumB / end)
    print('sumC: ', sumC / end)
    print('')

    print('timeA: ', time1 / end)
    print('timeB: ', time2 / end)
    print('timeC: ', time3 / end)
    print('timeD: ', time4 / end)



if __name__ == "__main__":
    main()
