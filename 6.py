
if __name__ == "__main__":

    with open("6.txt") as f:
        tdata = [x[:-1] for x in f]

    print(tdata)
    data=[]
    for d in tdata:
        sp = d.split(')')
        data.append(sp)
    print(data)
    total = 0
    for i,d in enumerate(data):
        x = d[0]
        s = d[1]
        total += 1
        w = 1
        while w != 0:
            print(i)
            f = 0
            for index, h in enumerate(data):
                if h[1] == x:
                    x = h[0]
                    s = h[1]
                    f = 1
                    total += 1
                    break
            if f == 0:
                w = 0

    print(total)