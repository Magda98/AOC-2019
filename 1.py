

from typing import List


if __name__ == "__main__":
    measurments: List[int] = []

    with open("1.txt", "r") as file:
        for line in file:
            measurments.append(int(line))

    count = 0
    for index, measurment in enumerate(measurments):
        if index == 0:
            pass
        elif measurment > measurments[index-1]:
            count += 1

    print('increased: {}'.format(count))

    # part2

    count = 0
    for index, measurment in enumerate(measurments):
        if index < 3:
            pass
        elif (measurments[index-3] + measurments[index-2]) + measurments[index-1] < (measurment + measurments[index-1] + measurments[index-2]):
            count += 1

    print('increased (windows): {}'.format(count))
