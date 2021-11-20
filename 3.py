import sys
import numpy as np
if __name__ == "__main__":

    with open("3.txt") as f:
        data = [list(x.strip().split(',')[0:]) for x in f]

    m = np.zeros([20000, 20000])
    cost = 0
    cross_found = 0
    data = data[::-1]
    for (w, d) in enumerate(data):
        startx = 10000
        starty = 10000
        for o in d:
            dir = o[:1]
            wi = int(o[1:])
            if dir == "R":
                for index in range(wi):
                    if m[starty, startx + index + 1] == 0 or m[starty, startx + index + 1] == w+1 :
                        m[starty, startx + index + 1] = w+1
                        if w == 1:
                            cost += 1
                    elif w == 1 and m[starty, startx + index + 1] == 1:
                        m[starty, startx + index + 1] = 3
                        cost +=1
                        print(cost)
                        cross_found = 1
                        break
                startx += wi
            if dir == "L":
                for index in range(wi):
                    if m[starty, startx - (index + 1)] == 0 or m[starty, startx - (index + 1)]  == w+1:
                        m[starty, startx - (index + 1)] = w+1
                        if w == 1:
                            cost += 1
                    elif w == 1 and m[starty, startx - (index + 1)] == 1:
                        m[starty, startx - (index + 1)] = 3
                        cost+=1
                        print(cost)
                        cross_found = 1
                        break
                startx -= wi
            if dir == "U":
                for index in range(wi):
                    if m[starty + index + 1, startx] == 0 or m[starty + index + 1, startx] == w+1:
                        m[starty + index + 1, startx] = w+1
                        if w == 1:
                            cost += 1
                    elif w == 1 and m[starty + index + 1, startx] == 1:
                        m[starty + index + 1, startx] = 3
                        cost+=1
                        print(cost)
                        cross_found = 1
                        break
                starty += wi
            if dir == "D":
                for index in range(wi):
                    if m[starty - (index + 1), startx] == 0 or  m[starty - (index + 1), startx] == w+1:
                        m[starty - (index + 1), startx] = w+1
                        if w == 1:
                            cost += 1
                    elif w == 1 and  m[starty - (index + 1), startx] == 1:
                        m[starty - (index + 1), startx] = 3
                        cost+=1
                        print(cost)
                        cross_found = 1
                        break
                starty -= wi
            if cross_found == 1:
                break

    for (w, d) in enumerate(data):
        startx = 10000
        starty = 10000
        for o in d:
            dir = o[:1]
            wi = int(o[1:])
            if dir == "R":
                for index in range(wi):
                    if m[starty, startx + index + 1] == 0 or m[starty, startx + index + 1] == w + 1:
                        m[starty, startx + index + 1] = w + 1
                        if w == 0:
                            cost += 1
                    elif  m[starty, startx + index + 1] == 3:
                        print(cost+1)
                        sys.exit()
                startx += wi
            if dir == "L":
                for index in range(wi):
                    if m[starty, startx - (index + 1)] == 0 or m[starty, startx - (index + 1)] == w + 1:
                        m[starty, startx - (index + 1)] = w + 1
                        if w == 0:
                            cost += 1
                    elif m[starty, startx - (index + 1)] == 3:
                        print(cost+1)
                        sys.exit()
                startx -= wi
            if dir == "U":
                for index in range(wi):
                    if m[starty + index + 1, startx] == 0 or m[starty + index + 1, startx] == w + 1:
                        m[starty + index + 1, startx] = w + 1
                        if w == 0:
                            cost += 1
                    elif m[starty + index + 1, startx] == 3:
                        print(cost+1)
                        sys.exit()
                starty += wi
            if dir == "D":
                for index in range(wi):
                    if m[starty - (index + 1), startx] == 0 or m[starty - (index + 1), startx] == w + 1:
                        m[starty - (index + 1), startx] = w + 1
                        if w == 0:
                            cost += 1
                    elif m[starty - (index + 1), startx] == 3:
                        print(cost+1)
                        sys.exit()
                starty -= wi


    starty = 1000
    startx = 1000
    leng = []
    for (indexr, r) in enumerate(m):
        for (indexc, c) in enumerate(r):
            if c == 3:
                leng.append(abs(indexr - starty) + abs(indexc - startx))
    print(min(leng))
    print(sorted(leng))