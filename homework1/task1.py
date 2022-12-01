from typing import List
import math


def nearest_zero(len_array: int, array: str) -> str:
    distances = [0 for i in range(len_array)]

    if array[0] == 0:
        distances[0] = 0
    else:
        distances[0] = math.inf

    # left-right traverse
    for i in range(1, len_array):
        distances[i] = distances[i - 1] + 1
        if array[i] == 0:
            distances[i] = 0

    # right-left traverse
    for i in range(len_array - 2, -1, -1):
        distances[i] = min(distances[i], distances[i + 1] + 1)

    return " ".join(map(str, distances))


if __name__ == '__main__':
    raw_input = input()
    arr = list(map(int, raw_input.split()))
    print(nearest_zero(len(arr), arr))
