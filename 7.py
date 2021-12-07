

from typing import List


if __name__ == "__main__":
    crabs: List[int] = []
    with open("7.txt", "r") as file:
        for i, l in enumerate(file):
            crabs = [int(x) for x in l.strip().split(",")]

    align = max(crabs)

    fuel_used = 10000000000000

    for crab_align in range(align):
        temp = 0
        for crab in crabs:
            temp_c = abs(crab_align - crab)
            temp += 0.5*(temp_c**2) + 0.5*temp_c

        if temp < fuel_used:
            fuel_used = temp

    print(fuel_used)
