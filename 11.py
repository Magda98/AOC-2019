import sys

import numpy as np
np.set_printoptions(threshold=sys.maxsize)
def split(word):
    return list(word)

if __name__ == "__main__":

    with open("11.txt") as f:
        tdata = list(map(int, f.readline().strip().split(',')))


    arr = np.zeros((5000,))
    arr[:len(tdata)] = np.array(tdata)

    data = arr.copy()

    panel = np.full((6,50),2)

    relative_base = 0
    temp = 0
    x = 0
    y = 0
    panel[y,x] = 1
    w = 0
    wi = -1
    kier = 0
    stop = 1
    ar = []
    while stop == 1:
        for (index, z) in enumerate(data):
            if temp == index:
                te = list(str(z))
                if len(te) >=2:
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
                    if panel[y, x] == 2:
                        we = 0
                    else:
                        we = panel[y, x]
                    if te[2] == "0":
                        data[int(data[index + 1])] = int(we)
                    elif te[2] == "1":
                        data[index + 1] = int(we)
                    elif te[2] == "2":
                        data[int(relative_base + data[index + 1])] = int(we)
                    temp = index + 2
                elif d == 4:
                    if te[2] == "0":
                        w = data[int(data[index + 1])]
                        wi+=1
                        # print(w)
                    elif te[2] == "1":
                        w = data[index + 1]
                        wi += 1
                        # print(w)
                    elif te[2] == "2":
                        w = data[int(relative_base + data[index + 1])]
                        wi += 1
                        # print(w)
                    temp = index + 2
                    if wi%2 == 0:
                        panel[y, x] = w
                        ar.append((y,x))
                    elif wi%2 == 1:
                        if w == 1:
                            if kier <= 2:
                                kier += 1
                            else:
                                kier = 0
                        else:
                            if kier > 0:
                                kier -=1
                            else:
                                kier = 3
                        if kier == 0:
                            y -= 1
                        elif kier == 1:
                            x += 1
                        elif kier == 2:
                            y += 1
                        elif kier == 3:
                            x -= 1


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

    # c=0
    # for d in panel:
    #     for p in d:
    #         if p ==1 or p ==0:
    #             c+=1
    #
    # print(c)
    print(panel)
