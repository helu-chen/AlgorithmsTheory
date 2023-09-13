import scaloneta
import matplotlib.pyplot as plt
from time import time
from random import randint

def getGraph():
    tests = []
    for i in range(1, 8):
        aux = []
        for _ in range (0, 10000*i):
            sI, aI = randint(0, 10000), randint(0, 10000)
            aux.append((sI, aI))
        tests.append(aux)

    start = time()
    
