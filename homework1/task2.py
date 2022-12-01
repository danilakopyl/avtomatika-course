from typing import List, Tuple


def sleight_of_hand(k: int, matrix: List[str]) -> int:
    numbers = {a: 0 for a in range(1, 10)}
    scores = 0
    for i in range(4):
        for j in matrix[i]:
            if j != '.':
                numbers[int(j)] += 1
    for i in numbers.values():
        if 0 < i <= 2 * k:
            scores += 1
    return scores


if __name__ == '__main__':
    number = int(input())
    matrix = [str(input()) for i in range(4)]
    print(sleight_of_hand(number, matrix))
