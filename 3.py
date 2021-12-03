from typing import List, Tuple
import numpy as np
from numpy.lib.function_base import append

if __name__ == "__main__":
    input: List[List[int]] = []

    with open("3.txt", "r") as file:
        for l in file:
            input.append([int(l[x]) for x in range(12)])

    input_np_x = np.array(input)
    input_np_y = input_np_x
    input_np = np.transpose(input_np_x)

    gamma = []
    epsilon = []
    for x in input_np:
        ones = 0
        zeros = 0
        for y in x:
            if y == 0:
                zeros += 1
            elif y == 1:
                ones += 1
        if zeros > ones:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

    dec_gamma = 0
    dec_epsilon = 0
    for index, x in enumerate(reversed(gamma)):
        dec_gamma += (2**index) * x
    for index, x in enumerate(reversed(epsilon)):
        dec_epsilon += (2**index) * x
    print(dec_gamma * dec_epsilon)

    oxygen = []
    for idx in range(12):
        zeros = 0
        ones = 0
        for x in input_np_x:
            if x[idx] == 0:
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            temp = []
            for x in input_np_x:
                if x[idx] == 0:
                    temp.append(x)
            input_np_x = temp
            oxygen = temp
        elif zeros == ones:
            temp = []
            for x in input_np_x:
                if x[idx] == 1:
                    temp.append(x)
            oxygen = temp
            break
        elif ones > zeros:
            temp = []
            for x in input_np_x:
                if x[idx] == 1:
                    temp.append(x)
            input_np_x = temp
            oxygen = temp

    print(oxygen)

    input_np_y
    oxygen = []
    for idx in range(12):
        zeros = 0
        ones = 0
        for x in input_np_y:
            if x[idx] == 0:
                zeros += 1
            else:
                ones += 1

        if zeros < ones:
            temp = []
            for x in input_np_y:
                if x[idx] == 0:
                    temp.append(x)
            input_np_y = temp
            oxygen = temp
        elif zeros == ones:
            temp = []
            for x in input_np_y:
                if x[idx] == 0:
                    temp.append(x)
            oxygen = temp
            break
        elif ones < zeros:
            temp = []
            for x in input_np_y:
                if x[idx] == 1:
                    temp.append(x)
            input_np_y = temp
            oxygen = temp

    print(oxygen)
