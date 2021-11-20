import itertools
import copy

if __name__ == "__main__":

    with open("5.txt") as f:
        tdata = list(map(int, f.readline().strip().split(',')))

    # tdata = copy.deepcopy(data)

    out = 0

    # a = range(100)
    # c = list(itertools.product(a, a))
    # for x in c:
    data = tdata.copy()
    #     data[1] = x[0]
    #     data[2] = x[1]
    temp = 0
    for (index, z) in enumerate(data):
        if temp == index:
            te = list(str(z))
            while len(te) <= 4:
                te.insert(0, "0")
            d = int(te[-1])
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
                data[data[index + 1]] = int(input())
                temp = index + 2
            elif d == 4:
                if te[2] == "0":
                    print(data[data[index + 1]])
                else:
                    print(data[index + 1])
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
                    data[data[index + 3]] = 0

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
                    data[data[index + 3]] = 0
                temp = index + 4

            elif d == 99:
                break

        # if data[0] == 19690720:
        #     print("found")
        #     break

    # print(data[0])
