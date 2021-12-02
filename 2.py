

from typing import List, Tuple


if __name__ == "__main__":
    directions: List[Tuple[str, int]] = []

    with open("2.txt", "r") as file:
        for line in file:
            items = line.split()
            directions.append((items[0], int(items[1])))

    hor = 0
    dep = 0
    calc_dep = []
    for direction in directions:
        if direction[0] == "forward":
            hor += direction[1]
            # second star
            calc_dep.append(direction[1] * dep)
        elif direction[0] == "down":
            dep += direction[1]
        elif direction[0] == "up":
            dep -= direction[1]

    temp = sum(calc_dep)
    print("depth: {}, horizontal: {}, multiply: {}".format(temp, hor, temp*hor))
