from math import sqrt

import numpy as np


def split(word):
    return list(word)


if __name__ == "__main__":

    with open("10-t.txt") as f:
        data = [split(line.rstrip('\n')) for line in f]

    # 46 - '.'
    # 35 - '#'

    data = np.array([list(map(ord, d)) for d in data])
    sum = 0
    data[data == 46] = 1
    data[data == 35] = 0
    print(data)
    for d in data:
        for val in d:
            if val == 0:
                sum += 1
    a = []
    ddd=[]
    mx = 0
    for x, d in enumerate(data):
        for y, val in enumerate(d):
            k1 = 0
            k2 = 0
            k3 = 0
            k4 = 0
            p = []
            l = []
            if val == 0 and x == 13 and y == 11:
                for row, r in enumerate(data):
                    for col, c in enumerate(r):
                        if c == 0 and x != row and y != col:
                            a = (y - col) / (x - row)
                            b = y - ((y - col) / (x - row)) * x
                            if col > y:
                                if ((a, b) in l):
                                    print("Element Exists")
                                else:
                                    l.append((a, b))
                                    ddd.append((col, row))
                            if col < y:
                                if ((a, b) in p):
                                    print("Element Exists")
                                else:
                                    p.append((a, b))
                                    ddd.append((col, row))
                        elif c == 0 and x == row:
                            if col > y:
                                  k1 = 1
                            if col < y:
                                  k2 = 1
                        elif c == 0 and y == col:
                            if row > x:
                                k3 = 1
                            if row < x:
                                k4 = 1

                if (len(p) + len(l)+ k1 + k2 + k3 + k4) > mx:
                    mx = len(p) + len(l) + k1 + k2 + k3 + k4
                    ind = (x, y)
    print((8,2) in ddd)
    print(mx, ind)
