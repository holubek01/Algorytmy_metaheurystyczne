import tsplib95
import random

def close_neighbour(optTour, matr, tour):
    for i in range(0, int(sizeTab) - 1):
        cls = matr[optTour[i]][tour[0]]
        optTour[i+1] = tour[0]
        if len(tour) > 1:
            for j in range(1, len(tour)):
                if matr[optTour[i]][tour[j]] < cls:
                    cls = matr[optTour[i]][tour[j]]
                    optTour[i + 1] = tour[j]
            tour.remove(optTour[i+1])

        else:
            optTour[i+1] = tour[0]
    return optTour


def fill_matrix(sizeTab, matr, l):
    for i in range(0, sizeTab):
        for j in range(0, sizeTab):
            edge = i + l, j + l
            matr[i][j] = problem.get_weight(*edge)


def destination(sizeTab, matr):
    weight = 0
    for i in range(0, int(sizeTab) - 1):
        weight += matr[optTour[i]][optTour[i + 1]]
    weight += matr[optTour[int(sizeTab) - 1]][optTour[0]]
    return weight

def opt2(swap_tour, i, j):
    help_zmienna = swap_tour[i]
    swap_tour[i] = swap_tour[j]
    swap_tour[j] = help_zmienna

    zmienna2 = destination2(len(swap_tour), matr, swap_tour)

    help_zmienna = swap_tour[i]
    swap_tour[i] = swap_tour[j]
    swap_tour[j] = help_zmienna

    return zmienna2


def destination2(sizeTab, matr, tour3):
    weight = 0
    for i in range(0, int(sizeTab) - 1):
        weight += matr[tour3[i]][tour3[i + 1]]

    weight += matr[tour3[int(sizeTab) - 1]][tour3[0]]
    return weight

def opt_swap(swap_tour, i, j):
    help_zmienna = swap_tour[i]
    swap_tour[i] = swap_tour[j]
    swap_tour[j] = help_zmienna

    return swap_tour


def koks_funkcja(acutal_tour):
    potential_tour = acutal_tour.copy()

    mini = opt2(acutal_tour, 0,1)
    k = 0
    l = 1


    for i in range(0, len(acutal_tour)):
        for j in range(i+1, len(acutal_tour)):
            potential_mini = opt2(acutal_tour, i, j)
            if potential_mini < mini:
                mini = potential_mini
                k = i
                l = j

    if(mini < destination2(len(potential_tour), matr, potential_tour)):
        koks_funkcja(opt_swap(acutal_tour,k,l))
    else:
        print(destination2(len(potential_tour), matr, potential_tour))
        print(potential_tour)


def result(tour):
    tour_copy = tour.copy()
    optTour[0] = tour[0]
    tour_copy.remove(tour[0])
    random.shuffle(tour_copy)
    close_neighbour(optTour, matr, tour_copy)
    mini2 = destination2(sizeTab, matr, optTour)

    droga = optTour
    for i in range(1, int(sizeTab)):
        tour_copy = tour.copy()
        optTour[0] = tour[i]
        tour_copy.remove(optTour[0])
        random.shuffle(tour_copy)
        close_neighbour(optTour, matr, tour_copy)
        if destination2(sizeTab, matr, optTour) < mini2:
            droga = optTour.copy()
            mini2 = destination2(sizeTab, matr, optTour)
    print(droga)
    print(destination2(sizeTab, matr, droga))
    print(mini2)
    print('')
    print('')
    koks_funkcja(droga)


#brazil58 - half matrix
#br17 - full matrix
#berlin52 - euclides

problem = tsplib95.load('C:\\ALL_tsp\\bier127.tsp\\bier127.tsp')

k = problem.is_full_matrix()
zmienna = list(problem.get_nodes())
sizeTab = len(zmienna)

tour = [0 for j in range(int(sizeTab))]
for i in range(0, int(sizeTab)):
    tour[i] = i
random.shuffle(tour)


optTour = [0 for j in range(int(sizeTab))]
matr = [[0 for _ in range(sizeTab)] for _ in range(sizeTab)]


if not k and not problem.is_explicit():
    fill_matrix(sizeTab, matr, 1)
else:
    fill_matrix(sizeTab, matr, 0)

result(tour)



#
# if not k:
#     if not problem.is_explicit():
#         fill_matrix(sizeTab, matr, 1)
#         result(tour)
#
#     else:
#         fill_matrix(sizeTab, matr, 0)
#         result(tour)
#
# else:
#
#     fill_matrix(sizeTab, matr,0)
#     result(tour)
