from math import sqrt

import numpy as np


def split(word):
    return list(word)


if __name__ == "__main__":

    with open("10.txt") as f:
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

    mx = 0
    x = 20
    y = 20
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    p = []
    wspp = []
    l = []
    wspl=[]
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

                if col < y:
                    if a == 3.1666666666666665 and b == -43.33333333333333:
                        wspp.append((row, col))
                    if ((a, b) in p):
                        print("Element Exists")
                    else:
                        p.append((a, b))
                        if row < x and col <= 3:
                            wspl.append((col, row))
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
    n = 0
    print(wspp)
    p = sorted(p, key=lambda x: x[0])
    p = p[::-1]
    l = sorted(l, key=lambda x: x[0])
    l = l[::-1]
    wspl = sorted(wspl, key=lambda x: x[0])
    print(wspl)
    while n < 201:
        for row, r in enumerate(data):
            for col, c in enumerate(r):
                n+=1


