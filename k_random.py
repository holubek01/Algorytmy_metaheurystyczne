import tsplib95
import sys
import random

mini = 10000


def fill_matrix(sizeTab, matr, l):
    for i in range(0, sizeTab):
        for j in range(0, sizeTab):
            edge = i + l, j + l
            matr[i][j] = problem.get_weight(*edge)


def destination(sizeTab, matr):
    weight = 0
    for i in range(0, int(sizeTab) - 1):
        weight += matr[tour[i]][tour[i + 1]]
    weight += matr[tour[int(sizeTab) - 1]][tour[0]]
    return weight



def k_random(sizeTab, matr, tour, mini):
    for i in range(0, 100000):
        random.shuffle(tour)
        weight = 0
        for i in range(0, int(sizeTab) - 1):
            weight += matr[tour[i]][tour[i + 1]]
        weight += matr[tour[int(sizeTab) - 1]][tour[0]]
        if weight < mini:
            mini = weight
    return mini

def result ():
    mini = destination(sizeTab, matr)
    mini = k_random(sizeTab, matr, tour, mini)
    print(mini)

problem = tsplib95.load('C:\\ALL_tsp\\bier127.tsp\\bier127.tsp')
#problem2 = tsplib95.load('C:\\Users\\holub\\OneDrive - Politechnika Wroclawska\\Desktop\\ALL_tsp\\brg180.opt.tour\\brg180.opt.tour')
k = problem.is_full_matrix()
zmienna = list(problem.get_nodes())
sizeTab = len(zmienna)

tour = [0 for j in range(int(sizeTab))]
for i in range(0, int(sizeTab)):
    tour[i] = i
random.shuffle(tour)
print(tour)
print(sizeTab)

matr = [[0 for _ in range(sizeTab)] for _ in range(sizeTab)]

if not k and not problem.is_explicit():
    fill_matrix(sizeTab, matr, 1)
else:
    fill_matrix(sizeTab, matr, 0)

result()



#if k:
 #   fill_matrix(sizeTab, matr, 1)
  #  mini = destination(sizeTab, matr, 1)
   # mini = k_random(sizeTab, matr, tour, mini, 1)
    #print(mini)
#else:
 #   fill_matrix(sizeTab, matr, 0)
  #  mini = destination(sizeTab, matr, 0)
   # mini = k_random(sizeTab, matr, tour, mini, 1)
    #print(mini)



 #for i in range(0, sizeTab):
        #    for j in range(0, sizeTab):
         #       edge = i + 1, j + 1
          #      matr[i][j] = problem.get_weight(*edge)

        #weight = 0
        #for i in range(0, int(sizeTab) - 1):
         #   weight += matr[tour[i] - 1][tour[i + 1] - 1]
        #weight += matr[tour[int(sizeTab) - 1] - 1][tour[0] - 1]
        #print(weight)