from typing import List, Tuple
import numpy as np
from numpy.lib.function_base import append

if __name__ == "__main__":
    board_list: List[List[List[int]]] = []
    input: List[int] = []
    temp: List[List[int]] = []
    with open("4.txt", "r") as file:
        for i, l in enumerate(file):
            if i == 0:
                tmp = l.strip().split(',')
                input = [int(i) for i in tmp]
            elif i > 1 and l != "\n":
                tmp = l.strip().split(' ')
                tmp_int: List[int] = []
                for x in tmp:
                    if x != '':
                        tmp_int.append(int(x))
                temp.append(tmp_int)
            elif i > 1 and l == "\n":
                board_list.append(temp)
                temp = []

    board_list = np.array(board_list)
    current_solution = 0
    number_called = 0
    stop = False
    board_check: List[bool] = [False for _ in range(board_list.shape[0])]
    for number in input:
        if stop:
            break
        for index, board in enumerate(board_list):
            for row in range(5):
                for col in range(5):
                    if board_list[index, row, col] == number:
                        board_list[index, row, col] = -1

        # check
        for index, board in enumerate(board_list):
            x = np.sum(board, axis=0).tolist()
            if -5 in x:
                number_called = number
                current_solution = index
                if board_check[index] == False:
                    current_solution = index
                    board_check[index] = True
                if False in board_check:
                    pass
                else:
                    stop = True
                    break
            y = np.sum(board, axis=1).tolist()
            if -5 in y:
                number_called = number
                if board_check[index] == False:
                    current_solution = index
                    board_check[index] = True
                if False in board_check:
                    pass
                else:
                    stop = True
                    break

    array_sum = np.where(board_list[current_solution] < 0, 0, board_list[current_solution])
    array_sum = np.sum(array_sum)

    print("solution Bingo!: {}".format(array_sum*number_called))
