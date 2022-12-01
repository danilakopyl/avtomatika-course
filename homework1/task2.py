from typing import List, Tuple


def sleight_of_hand(k: int, matrix: str) -> int:
    numbers = {a: 0 for a in range(1, 10)}
    matrix = [line.strip() for line in matrix.split("\n")]
    scores = 0
    for i in range(4):
        for j in matrix[i]:
            if j != '.':
                numbers[int(j)] += 1
    for i in numbers.values():
        if 0 < i <= 2 * k:
            scores += 1
    return scores


def read_input():
    number = int(input())
    matrix = [str(input()) for i in range(4)]
    return number, matrix


if __name__ == '__main__':
    #print(sleight_of_hand(*read_input()))
    matrix = [str(input()) for i in range(4)]
    type(matrix)
    print(matrix)
