


if __name__ == "__main__":

    passwd = range(382345, 843167)
    good_passwd = 0
    for x in passwd:
        st = str(x)
        dig_l = -1
        same = 0
        good = 0
        dig_prev = -1
        dig_next = -1
        for index, d in enumerate(st):
            if index >= 2:
                dig_prev = int(st[index-2])
            else:
                dig_prev = -1
            if index <= 4:
                dig_next = int(st[index+1])
            else:
                dig_next = -1
            dig_c = int(d)
            if dig_c > dig_l:
                good = 1
            elif (dig_c == dig_l and dig_next != dig_c and dig_prev != dig_c ):
                same = 1
            elif dig_c < dig_l:
                good = 0
                break
            dig_l = dig_c
        if same == 1 and good == 1 :
            good_passwd+=1

    print(good_passwd)

