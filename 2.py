import itertools
import copy
if __name__ == "__main__":

    with open("2.txt") as f:
        tdata = list( map(int, f.readline().strip().split(',')))



    # tdata = copy.deepcopy(data)

    out = 0

    a = range(100)
    c = list(itertools.product(a, a))
    for x in c:
        data = tdata.copy()
        data[1] = x[0]
        data[2] = x[1]
        temp = 0
        for (index,d) in enumerate(data):
            if temp == index:
               if d == 1:
                   data[data[index+3]] = data[data[index+1]] + data[data[index+2]]
                   temp = index+4
               elif d == 2:
                   data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
                   temp = index+4
               elif d == 99:
                   break

        if data[0] == 19690720:
            print("found")
            break

    print(100*data[1] + data[2])