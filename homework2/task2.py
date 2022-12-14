from typing import List, Optional


def compare(n1: Optional[int, str], n2: Optional[int, str]):
    # custom comparator
    return n1 + n2 > n2 + n1


def get_largest_combination(nums: List[int]) -> str:
    # insertion sort
    for i in range(len(nums)):
        pos, cur = i, nums[i]
        while pos > 0 and not compare(nums[pos-1], cur):
            nums[pos] = nums[pos-1]
            pos -= 1
        nums[pos] = cur
    return str(int("".join(map(str, nums))))


if __name__ == '__main__':
    print(get_largest_combination([30,39]))
