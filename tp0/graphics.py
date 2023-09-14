import matplotlib.pyplot as plt
from random import randint
from time import time
import scaloneta

NUMTESTS = 10
MIN = 1000
MAX = 10000
AX = [MAX*i for i in range(1, NUMTESTS+1)]

def getGraph():
    tests = []
    for i in range(1, NUMTESTS+1):
        aux = []
        for _ in range(MAX*i):
            aux.append((randint(MIN, MAX), randint(MIN, MAX)))
        tests.append(aux)

    times = []
    for i in range(len(tests)):
        start = time()
        scaloneta.main(tests[i])
        end = time()
        dt = end - start
        times.append(dt)


    fig, ax = plt.subplots()
    ax.plot(AX, times, label= 'Greedy Algorithm')
    ax.set(xlabel='quantity of videos', ylabel='time(s)', title='Complexity of the algorithm')
    ax.grid()
    
    fig.savefig('graphic.png')
    plt.legend()
    plt.show()


getGraph()

