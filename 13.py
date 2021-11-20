import sys

import numpy as np
np.set_printoptions(threshold=sys.maxsize)
def split(word):
    return list(word)

if __name__ == "__main__":

    with open("13.txt") as f:
        tdata = list(map(int, f.readline().strip().split(',')))


    arr = np.zeros((5000,))
    arr[:len(tdata)] = np.array(tdata)

    data = arr.copy()
    count = 0
    wy = 0
    stop = 1
    temp = 0
    relative_base = 0
    wi = 0
    wy1 = 0
    wy2 = 0
    wy3 = 0
    while stop == 1:
        for (index, z) in enumerate(data):
            if temp == index:
                te = list(str(z))
                if te[-2] == ".":
                    te = te[0:-2]
                while len(te) <= 4:
                    te.insert(0, "0")
                l1 = int(te[-1])
                l2 = int(te[-2])
                d = l2 * 10 + l1
                if d == 1:
                    if te[2] == "0":
                        n1 = data[int(data[index + 1])]
                    elif te[2] == "1":
                        n1 = data[index + 1]
                    elif te[2] == "2":
                        n1 = data[int(relative_base + data[index + 1])]
                    if te[1] == "0":
                        n2 = data[int(data[index + 2])]
                    elif te[1] == "1":
                        n2 = data[index + 2]
                    elif te[1] == "2":
                        n2 = data[int(relative_base + data[index + 2])]
                    if te[0] == "0":
                        data[int(data[index + 3])] = n1 + n2
                    if te[0] == "1":
                        data[index + 3] = n1 + n2
                    if te[0] == "2":
                        data[int(relative_base + data[index + 3])] = n1 + n2

                    temp = index + 4
                elif d == 2:
                    if te[2] == "0":
                        n1 = data[int(data[index + 1])]
                    elif te[2] == "1":
                        n1 = data[index + 1]
                    elif te[2] == "2":
                        n1 = data[int(relative_base + data[index + 1])]
                    if te[1] == "0":
                        n2 = data[int(data[index + 2])]
                    elif te[1] == "1":
                        n2 = data[index + 2]
                    elif te[1] == "2":
                        n2 = data[int(relative_base + data[index + 2])]
                    if te[0] == "0":
                        data[int(data[index + 3])] = n1 * n2
                    if te[0] == "1":
                        data[index + 3] = n1 * n2
                    if te[0] == "2":
                        data[int(relative_base + data[index + 3])] = n1 * n2

                    temp = index + 4
                elif d == 3:
                    if te[2] == "0":
                        data[int(data[index + 1])] = int(input())
                    elif te[2] == "1":
                        data[index + 1] = int(input())
                    elif te[2] == "2":
                        data[int(relative_base + data[index + 1])] = int(input())
                    temp = index + 2
                elif d == 4:
                    if te[2] == "0":
                        wy = data[int(data[index + 1])]
                        print()
                    elif te[2] == "1":
                        wy =  data[index + 1]
                        print()
                    elif te[2] == "2":
                        wy = data[int(relative_base + data[index + 1])]
                        print()
                    if  wi%3 == 0:
                       wy1 = wy
                    if  wi%3 == 1:
                        wy2 = wy
                    if wi%3 == 2 and wy2 == 0 and wy1 == -1:
                        print(wy)
                    if wy == 2 and wi%3 == 2 :
                        count += 1
                    temp = index + 2
                    wi += 1
                elif d == 5:
                    if te[2] == "0":
                        n1 = data[int(data[index + 1])]
                    elif te[2] == "1":
                        n1 = data[index + 1]
                    elif te[2] == "2":
                        n1 = data[int(relative_base + data[index + 1])]
                    if te[1] == "0":
                        n2 = data[int(data[index + 2])]
                    elif te[1] == "1":
                        n2 = data[index + 2]
                    elif te[1] == "2":
                        n2 = data[int(relative_base + data[index + 2])]
                    if n1 != 0:
                        temp = n2
                    else:
                        temp = index + 3
                elif d == 6:
                    if te[2] == "0":
                        n1 = data[int(data[index + 1])]
                    elif te[2] == "1":
                        n1 = data[index + 1]
                    elif te[2] == "2":
                        n1 = data[int(relative_base + data[index + 1])]
                    if te[1] == "0":
                        n2 = data[int(data[index + 2])]
                    elif te[1] == "1":
                        n2 = data[index + 2]
                    elif te[1] == "2":
                        n2 = data[int(relative_base + data[index + 2])]
                    if n1 == 0:
                        temp = n2
                    else:
                        temp = index + 3
                elif d == 7:
                    if te[2] == "0":
                        n1 = data[int(data[index + 1])]
                    elif te[2] == "1":
                        n1 = data[index + 1]
                    elif te[2] == "2":
                        n1 = data[int(relative_base + data[index + 1])]
                    if te[1] == "0":
                        n2 = data[int(data[index + 2])]
                    elif te[1] == "1":
                        n2 = data[index + 2]
                    elif te[1] == "2":
                        n2 = data[int(relative_base + data[index + 2])]
                    if n1 < n2:
                        if te[0] == "0":
                            data[int(data[index + 3])] = 1
                        elif te[0] == "1":
                            data[index + 3] = 1
                        elif te[0] == "2":
                            data[int(relative_base + data[index + 3])] = 1
                    else:
                        if te[0] == "0":
                            data[int(data[index + 3])] = 0
                        elif te[0] == "1":
                            data[index + 3] = 0
                        elif te[0] == "2":
                            data[int(relative_base + data[index + 3])] = 0

                    temp = index + 4

                elif d == 8:
                    if te[2] == "0":
                        n1 = data[int(data[index + 1])]
                    elif te[2] == "1":
                        n1 = data[index + 1]
                    elif te[2] == "2":
                        n1 = data[int(relative_base + data[index + 1])]
                    if te[1] == "0":
                        n2 = data[int(data[index + 2])]
                    elif te[1] == "1":
                        n2 = data[index + 2]
                    elif te[1] == "2":
                        n2 = data[int(relative_base + data[index + 2])]
                    if n1 == n2:
                        if te[0] == "0":
                            data[int(data[index + 3])] = 1
                        elif te[0] == "1":
                            data[index + 3] = 1
                        elif te[0] == "2":
                            data[int(relative_base + data[index + 3])] = 1
                    else:
                        if te[0] == "0":
                            data[int(data[index + 3])] = 0
                        elif te[0] == "1":
                            data[index + 3] = 0
                        elif te[0] == "2":
                            data[int(relative_base + data[index + 3])] = 0
                    temp = index + 4
                elif d == 9:
                    if te[2] == "0":
                        relative_base += data[int(data[index + 1])]
                    elif te[2] == "1":
                        relative_base += data[index + 1]
                    elif te[2] == "2":
                        relative_base += data[int(relative_base + data[index + 1])]
                    temp = index + 2
                elif d == 99:
                    stop = 0
                    break

    print(count)