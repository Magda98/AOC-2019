import  numpy as np
def split(word):
    return [int(char) for char in word]

if __name__ == "__main__":

    with open("8.txt") as f:
        tdata = list( split(f.readline()))

    tdata = np.array(tdata)

    tdata = tdata.reshape(100, 6, 25)

    # mi = 9999999
    # ind = -1
    message = np.full((6,25), 2)
    for index,d in enumerate(tdata):
        # z = 0
        for i,x in enumerate(d):
            for k, y in enumerate(x):
                if message[i, k] == 2:
                    message[i, k] = y
                # if y == 0:
                #     z+=1

        # if z < mi:
        #     mi = z
        #     ind = index

    # print(ind)
    print(message)

    # o = 0
    # t = 0
    # for i, x in enumerate(tdata[12]):
    #     for k, y in enumerate(x):
    #         if y == 1:
    #             o+=1
    #         if y == 2:
    #             t+=1
    #
    # print(o*t)
