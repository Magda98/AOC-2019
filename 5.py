from typing import List, Tuple
import numpy as np
import math
from numpy.lib.function_base import append

if __name__ == "__main__":
    start: List[List[int]] = []
    end: List[List[int]] = []
    with open("5.txt", "r") as file:
        for i, l in enumerate(file):
            temp = l.strip().split(" -> ")
            start.append([int(x) for x in temp[0].split(",")])
            end.append([int(x) for x in temp[1].split(",")])

    tab = np.zeros((1000, 1000), dtype=int)

    for x, y in zip(start, end):
        if x[0] == y[0]:
            if y[1] > x[1]:
                for i in range(x[1], y[1] + 1, 1):
                    tab[i, x[0]] += 1
            else:
                for i in range(y[1], x[1] + 1, 1):
                    tab[i, x[0]] += 1
        elif x[1] == y[1]:
            if y[0] > x[0]:
                for i in range(x[0], y[0] + 1, 1):
                    tab[x[1], i] += 1
            else:
                for i in range(y[0], x[0] + 1, 1):
                    tab[x[1], i] += 1
        else:
            s1 = x[0] if y[0] > x[0] else y[0]
            e1 = x[0] if y[0] < x[0] else y[0]
            s2 = x[1] if y[1] > x[1] else y[1]
            e2 = x[1] if y[1] < x[1] else y[1]

            sx = s1
            sy = s2
            if (x[0] > y[0] and x[1] > y[1]) or (x[0] < y[0] and x[1] < y[1]):
                for i in range(s1, e1+1, 1):
                    for j in range(s2, e2 + 1, 1):
                        if (i - sx) == (j - sy):
                            tab[j, i] += 1
            else:
                size = e1 - s1
                if x[0] < y[0]:
                    for i in range(size+1):
                        tab[x[1]-i, x[0]+i] += 1
                else:
                    for i in range(size+1):
                        tab[x[1]+i, x[0]-i] += 1

    tab = np.where(tab < 2, 0, tab)
    array_sum = np.where(tab >= 2, 1, tab)
    print("rozwiązanie: {}".format(np.sum(array_sum)))
