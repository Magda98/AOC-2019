import itertools
import copy

if __name__ == "__main__":

    with open("7-t.txt") as f:
        tdata = list(map(int, f.readline().strip().split(',')))

    out = -999
    mx= []
    a = range(5)
    b = range (5, 10, 1)
    dd = list(itertools.permutations(b))
    c = list(itertools.permutations(a))
    print(len(c))
    for t,x in enumerate(c):
        we = 0
        f = 0
        data = tdata.copy()
        we1 = 0
        for k,inp in enumerate(x):
            temp = 0
            f+=1
            p = 1
            for (index, z) in enumerate(data):
                if temp == index:
                    te = list(str(z))
                    while len(te) <= 4:
                        te.insert(0, "0")
                    l1 = int(te[-1])
                    l2 = int(te[-2])
                    d = l2 * 10 + l1
                    if d == 1:
                        if te[2] == "0":
                            n1 = data[data[index + 1]]
                        else:
                            n1 = data[index + 1]
                        if te[1] == "0":
                            n2 = data[data[index + 2]]
                        else:
                            n2 = data[index + 2]
                        if te[0] == "0":
                            data[data[index + 3]] = n1 + n2
                        if te[0] == "1":
                            data[index + 3] = n1 + n2

                        temp = index + 4
                    elif d == 2:
                        if te[2] == "0":
                            n1 = data[data[index + 1]]
                        else:
                            n1 = data[index + 1]
                        if te[1] == "0":
                            n2 = data[data[index + 2]]
                        else:
                            n2 = data[index + 2]
                        if te[0] == "0":
                            data[data[index + 3]] = n1 * n2
                        if te[0] == "1":
                            data[index + 3] = n1 * n2

                        temp = index + 4
                    elif d == 3:
                        if p == 1:
                            if te[2] == "0":
                                data[int(data[index + 1])] = int(inp)
                            elif te[2] == "1":
                                data[index + 1] = int(inp)
                            p = 0
                        else:
                            if te[2] == "0":
                                data[int(data[index + 1])] = int(we)
                            elif te[2] == "1":
                                data[index + 1] = int(we)

                        temp = index + 2
                    elif d == 4:
                        if te[2] == "0":
                            we = data[data[index + 1]]
                            if k == 4:
                                we1 = we
                        else:
                            we = data[index + 1]
                            if k == 4:
                                 we1 = we
                        temp = index + 2
                    elif d == 5:
                        if te[2] == "0":
                            n1 = data[data[index + 1]]
                        else:
                            n1 = data[index + 1]
                        if te[1] == "0":
                            n2 = data[data[index + 2]]
                        else:
                            n2 = data[index + 2]
                        if n1 != 0:
                            temp = n2
                        else:
                            temp = index + 3
                    elif d == 6:
                        if te[2] == "0":
                            n1 = data[data[index + 1]]
                        else:
                            n1 = data[index + 1]
                        if te[1] == "0":
                            n2 = data[data[index + 2]]
                        else:
                            n2 = data[index + 2]
                        if n1 == 0:
                            temp = n2
                        else:
                            temp = index + 3
                    elif d == 7:
                        if te[2] == "0":
                            n1 = data[data[index + 1]]
                        else:
                            n1 = data[index + 1]
                        if te[1] == "0":
                            n2 = data[data[index + 2]]
                        else:
                            n2 = data[index + 2]
                        if n1 < n2:
                            if te[0] == "0":
                                data[data[index + 3]] = 1
                            else:
                                data[index + 3] = 1
                        else:
                            if te[0] == "0":
                                data[data[index + 3]] = 0
                            else:
                                data[index + 3] = 0

                        temp = index + 4

                    elif d == 8:
                        if te[2] == "0":
                            n1 = data[data[index + 1]]
                        else:
                            n1 = data[index + 1]
                        if te[1] == "0":
                            n2 = data[data[index + 2]]
                        else:
                            n2 = data[index + 2]
                        if n1 == n2:
                            if te[0] == "0":
                                data[data[index + 3]] = 1
                            else:
                                data[index + 3] = 1
                        else:
                            if te[0] == "0":
                                data[data[index + 3]] = 0
                            else:
                                data[index + 3] = 0
                        temp = index + 4

                    elif d == 99:
                        break

        if f == 5:
            for (a, r) in enumerate(dd):
                we = we1
                st = 1
                fir = 0
                wy = 0
                data1 = tdata.copy()
                while st == 1:
                    for (g, inp2) in enumerate(r):
                        print(a, inp2, g)
                        temp = 0
                        p = 1
                        for (index, z) in enumerate(data1):
                            if temp == index:
                                te = list(str(z))
                                while len(te) <= 4:
                                    te.insert(0, "0")

                                l1 = int(te[-1])
                                l2 = int(te[-2])
                                d = l2*10 + l1
                                if d == 1:
                                    if te[2] == "0":
                                        n1 = data1[data1[index + 1]]
                                    else:
                                        n1 = data1[index + 1]
                                    if te[1] == "0":
                                        n2 = data1[data1[index + 2]]
                                    else:
                                        n2 = data1[index + 2]
                                    if te[0] == "0":
                                        data1[data1[index + 3]] = n1 + n2
                                    if te[0] == "1":
                                        data1[index + 3] = n1 + n2

                                    temp = index + 4
                                elif d == 2:
                                    if te[2] == "0":
                                        n1 = data1[data1[index + 1]]
                                    else:
                                        n1 = data1[index + 1]
                                    if te[1] == "0":
                                        n2 = data1[data1[index + 2]]
                                    else:
                                        n2 = data1[index + 2]
                                    if te[0] == "0":
                                        data1[data1[index + 3]] = n1 * n2
                                    if te[0] == "1":
                                        data1[index + 3] = n1 * n2

                                    temp = index + 4
                                elif d == 3:
                                    # if fir == 0:
                                    if p == 1:
                                        if te[2] == "0":
                                            data[int(data[index + 1])] = int(inp2)
                                        elif te[2] == "1":
                                            data[index + 1] = int(inp2)
                                        p = 0
                                    else:
                                        if te[2] == "0":
                                            data[int(data[index + 1])] = int(we1)
                                        elif te[2] == "1":
                                            data[index + 1] = int(we1)

                                        if g == 4:
                                            fir = 1
                                    # elif fir == 1:
                                    #    data1[data1[index + 1]] = int(we)
                                    temp = index + 2
                                elif d == 4:
                                    if te[2] == "0":
                                        we = data1[data1[index + 1]]
                                        if g == 4:
                                            wy = we
                                    else:
                                        we = data1[index + 1]
                                        if g == 4:
                                            wy = we
                                    temp = index + 2
                                elif d == 5:
                                    if te[2] == "0":
                                        n1 = data1[data1[index + 1]]
                                    else:
                                        n1 = data1[index + 1]
                                    if te[1] == "0":
                                        n2 = data1[data1[index + 2]]
                                    else:
                                        n2 = data1[index + 2]
                                    if n1 != 0:
                                        temp = n2
                                    else:
                                        temp = index + 3
                                elif d == 6:
                                    if te[2] == "0":
                                        n1 = data1[data1[index + 1]]
                                    else:
                                        n1 = data1[index + 1]
                                    if te[1] == "0":
                                        n2 = data1[data1[index + 2]]
                                    else:
                                        n2 = data1[index + 2]
                                    if n1 == 0:
                                        temp = n2
                                    else:
                                        temp = index + 3
                                elif d == 7:
                                    if te[2] == "0":
                                        n1 = data1[data1[index + 1]]
                                    else:
                                        n1 = data1[index + 1]
                                    if te[1] == "0":
                                        n2 = data1[data1[index + 2]]
                                    else:
                                        n2 = data1[index + 2]
                                    if n1 < n2:
                                        if te[0] == "0":
                                            data1[data1[index + 3]] = 1
                                        else:
                                            data1[index + 3] = 1
                                    else:
                                        if te[0] == "0":
                                            data1[data1[index + 3]] = 0
                                        else:
                                            data1[index + 3] = 0

                                    temp = index + 4

                                elif d == 8:
                                    if te[2] == "0":
                                        n1 = data1[data1[index + 1]]
                                    else:
                                        n1 = data1[index + 1]
                                    if te[1] == "0":
                                        n2 = data1[data1[index + 2]]
                                    else:
                                        n2 = data1[index + 2]
                                    if n1 == n2:
                                        if te[0] == "0":
                                            data1[data1[index + 3]] = 1
                                        else:
                                            data1[index + 3] = 1
                                    else:
                                        if te[0] == "0":
                                            data1[data1[index + 3]] = 0
                                        else:
                                            data1[index + 3] = 0
                                    temp = index + 4
                                elif d == 99:
                                    st = 0
                                    break
                            if st == 0:
                                print("stop")
                                break
                        if st == 0:
                            print("stop")
                            break
                    if out < wy:
                        out = wy
                        ind = r





    # print(data[0])
    print(out, ind)