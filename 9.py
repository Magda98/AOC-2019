import itertools
import copy
import numpy as np

if __name__ == "__main__":

    with open("9.txt") as f:
        tdata = list(map(int, f.readline().strip().split(',')))

    # tdata = copy.deepcopy(data)

    out = 0
    arr = np.zeros((20000,))
    arr[:len(tdata)] = np.array(tdata)

    # a = range(100)
    # c = list(itertools.product(a, a))
    # for x in c:
    data = arr.copy()
    #     data[1] = x[0]
    #     data[2] = x[1]
    # print(data)
    stop = 1
    relative_base = 0
    temp = 0
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
                        print(data[int(data[index + 1])])
                    elif te[2] == "1":
                        print(data[index + 1])
                    elif te[2] == "2":
                        print(data[int(relative_base + data[index + 1])])
                    temp = index + 2
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

    # print(data[0])
