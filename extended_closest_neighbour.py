import tsplib95
import random

def close_neighbour(optTour, matr, tour_copy):
    for i in range(0, int(sizeTab) - 1):
        cls = matr[optTour[i]][tour_copy[0]]
        optTour[i+1] = tour_copy[0]
        if len(tour_copy) > 1:
            for j in range(1, len(tour_copy)):
                if matr[optTour[i]][tour_copy[j]] < cls:
                    cls = matr[optTour[i]][tour_copy[j]]
                    optTour[i + 1] = tour_copy[j]                    #j jest najblizszym sasaidem
            tour_copy.remove(optTour[i+1])

        else:
            optTour[i+1] = tour_copy[0]
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

def result(tour):
    tour_copy = tour.copy()                         #wez kopie a nie wskaznik
    optTour[0] = tour[0]
    tour_copy.remove(tour[0])
    random.shuffle(tour_copy)
    close_neighbour(optTour, matr, tour_copy)
    mini = destination(sizeTab, matr)

    for i in range(1, int(sizeTab)):
        tour_copy = tour.copy()
        optTour[0] = tour[i]
        tour_copy.remove(optTour[0])
        random.shuffle(tour_copy)
        close_neighbour(optTour, matr, tour_copy)
        if destination(sizeTab, matr) < mini:
            mini = destination(sizeTab,matr)
    print(mini)




#brazil58 - half matrix
#br17 - full matrix
#berlin52 - euclides

problem = tsplib95.load('C:\\Users\\holub\\OneDrive - Politechnika Wroclawska\\Desktop\\ALL_tsp\\berlin52.tsp\\berlin52.tsp')
#problem2 = tsplib95.load('C:/Users/piotr/Desktop/Meta/brg180.opt.tour')
k = problem.is_full_matrix()
zmienna = list(problem.get_nodes())
sizeTab = len(zmienna)

tour = [0 for j in range(int(sizeTab))]
for i in range(0, int(sizeTab)):
    tour[i] = i


optTour = [0 for j in range(int(sizeTab))]
matr = [[0 for _ in range(sizeTab)] for _ in range(sizeTab)]


if not k and not problem.is_explicit():
    fill_matrix(sizeTab, matr, 1)
else:
    fill_matrix(sizeTab, matr, 0)

result(tour)

