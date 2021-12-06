
from typing import List


if __name__ == "__main__":
    herd: List[int] = []
    with open("6.txt", "r") as file:
        for i, l in enumerate(file):
            herd = [int(x) for x in l.strip().split(",")]

    days = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]

    for x in herd:
        for d in days:
            if d[0] == x:
                d[1] += 1
    new_fish = 0
    for _ in range(256):
        for i, x in enumerate(days):
            if x[0] == 0:
                days[7][1] += x[1]
                new_fish = x[1]
            elif x[0] > 0:
                days[i-1][1] = x[1]
                if x[0] == 8:
                    days[i][1] = new_fish

    s = 0
    for x in days:
        s += x[1]

    print(s)
