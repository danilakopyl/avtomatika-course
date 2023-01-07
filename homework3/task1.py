def int_to_bin(x: int) -> str:
    if x == 0:
        return '0'
    bit = []
    while x:
        bit.append(str(x % 2))
        x //= 2
    return ''.join(bit[::-1])


if __name__ == '__main__':
    for i in range(10):
        print(int_to_bin(i))
