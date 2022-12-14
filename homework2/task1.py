from typing import List


def generate_parentheses(n: int) -> List[str]:
    stack = []
    result = []

    def helper(n_open, n_close):
        if n_open == n_close == n:
            result.append(''.join(stack))
            return

        if n_open < n:
            stack.append('(')
            helper(n_open + 1, n_close)
            stack.pop()

        if n_close < n_open:
            stack.append(')')
            helper(n_open, n_close + 1)
            stack.pop()

    helper(0, 0)
    return result


if __name__ == '__main__':
    print(generate_parentheses(3))
