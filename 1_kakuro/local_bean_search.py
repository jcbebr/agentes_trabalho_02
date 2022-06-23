import random
import time
from karuko import load_from_file, Karuko
from sys import argv

class Exec:
    def __init__(self, valid, ka):
        self.is_valid = valid
        self.ka = ka

def lbs(ka: Karuko, k, timer = 5, seed = 123):
    start = time.process_time()
    random.seed(seed)

    solutions = []
    for i in range(k):
        temp = ka.copy()
        temp.randomSolution()
        solutions.append(temp)

    while True:
        if time.process_time() - start < timer:
            neib = []
            for r in solutions:
                neib = neib + r.getNeib2()

            neib.sort(key=mySort)
            if neib[0].rb == 0:
                return Exec(True, neib[0])
            solutions = neib[0:k]
            del neib
        else:
            break

    best = solutions[0]
    return Exec(False, best)

def mySort(k):
    return k.rb

ka = load_from_file('dataset\\'+argv[1])
exec = lbs(ka, int(argv[2]), int(argv[3]), int(argv[4]))
print(exec.ka)
if not(exec.is_valid):
    print('Resultado não é completo. Número de inconsistências: ' + str(exec.ka.rb))
