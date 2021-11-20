import math

if __name__ == "__main__":

    data = [line.rstrip('\n') for line in open("1.txt")]
    data = list(map(float, data))

    sum=0
    for d in data:
        temp = d
        while temp > 0:
            temp = math.floor(temp/3) -2
            if temp > 0:
                sum+= temp


    print(sum)