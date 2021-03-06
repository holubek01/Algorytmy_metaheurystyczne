import random
import time
import tsplib95

problem = tsplib95.load('C:\\ALL_tsp\\bier127.tsp\\bier127.tsp')

k = problem.is_full_matrix()
zmienna = list(problem.get_nodes())
sizeTab = len(zmienna)
end = 10
licznik = 0

il = 3
matr2 = [[0 for _ in range(il)] for _ in range(il)]
for i in range(il):
    for j in range(il):
        matr2[i][j] = random.randint(1,1000)

sumA = 0
sumB = 0
sumC = 0
sumD = 0
time1 = 0
time2 = 0
time3 = 0
time4 = 0

tour = [0 for j in range(int(sizeTab))]
optTour = [0 for j in range(int(sizeTab))]
matr = [[0 for _ in range(sizeTab)] for _ in range(sizeTab)]


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

    global a4
    a4 = time.time()
    for i in range(0, len(acutal_tour)):
        for j in range(i+1, len(acutal_tour)):
            potential_mini = opt2(acutal_tour, i, j)
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
    if(mini < destination2(len(potential_tour), matr, potential_tour)):
        koks_funkcja(opt_swap(acutal_tour,k,l))
    else:
        global sumC
        sumC += destination2(len(potential_tour), matr, potential_tour)



def result(tour):
    tour_copy = tour.copy()
    tour_copy_2 = tour.copy()

    random.shuffle(tour_copy_2)
    optTour[0] = tour_copy_2[0]
    tour_copy_2.remove(tour_copy_2[0])
    global a1
    a1 = time.time()
    close_neighbour(optTour, matr, tour_copy_2)
    global b1
    b1 = time.time()
    global time1
    time1 += ((b1-a1)*1000)
    destination2(sizeTab, matr, optTour)
    global sumA
    sumA +=destination2(sizeTab, matr, optTour)


    global a2
    a2 = time.time()
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
    global b2
    b2 = time.time()
    global time2
    time2 += ((b2 - a2) * 1000)

    global sumB
    sumB += destination2(sizeTab, matr, droga)

    global a3
    a3 = time.time()
    koks_funkcja(droga)
    global b3
    b3 = time.time()
    global time3
    time3 += ((b3 - a3) * 1000)

def main():

    print(matr2)

    for i in range(0, end):
        for i in range(0, int(sizeTab)):
            tour[i] = i
        random.shuffle(tour)

        if not k and not problem.is_explicit():
            fill_matrix(sizeTab, matr, 1)
        else:
            fill_matrix(sizeTab, matr, 0)

        result(tour)

    print('sumA:')
    print(sumA/end)

    print('sumB:')
    print(sumB/end)

    print('sumC:')
    print(sumC/end)

    print('sumD:')
    print(sumD / end)

    print('')

    print('timeA:')
    print(time1/end)

    print('timeB:')
    print(time2/end)

    print('timeC:')
    print(time3/end)

    print('timeD:')
    print(time4 / licznik)


if __name__=="__main__":
    main()
