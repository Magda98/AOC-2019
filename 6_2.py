
if __name__ == "__main__":

    with open("6.txt") as f:
        tdata = [x[:-1] for x in f]

    print(tdata)
    data=[]
    for d in tdata:
        sp = d.split(')')
        data.append(sp)
    print(data)
    you = set()
    san = set()
    for i,d in enumerate(data):
        x = d[0]
        s = d[1]
        w = 1
        if s == "YOU":
            while w != 0:
                print(i)
                f = 0
                for index, h in enumerate(data):
                    if h[1] == x:
                        you.add(x)
                        x = h[0]
                        s = h[1]
                        f = 1
                        break
                if f == 0:
                    w = 0
        elif s == "SAN":
            while w != 0:
                print(i)
                f = 0
                for index, h in enumerate(data):
                    if h[1] == x:
                        san.add(x)
                        x = h[0]
                        s = h[1]
                        f = 1
                        break
                if f == 0:
                    w = 0


    print(len(you.symmetric_difference(san)))