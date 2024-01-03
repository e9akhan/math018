"""
    Module name :- solver
    Method(s) :- backtrack(matrix, x, y), solver(num)
"""


def backtrack(matrix, x, y):
    """
    Find the sum of number at current node and next node.

    Args:
        matrix(list) :- Matrix storing number
        x(int) :- Vertical position of node.
        y(int) :- Horizontal poistion of node.

    Return:
        Sum of number at current node and next node.
    """
    if x == len(matrix) - 1:
        return int(matrix[x][y])

    return int(matrix[x][y]) + max(
        backtrack(matrix, x + 1, y), backtrack(matrix, x + 1, y + 1)
    )


def solver(num):
    """
    Find the maximum sum of number in given matrix.

    Args:
        num(str) :- String of numbers

    Return:
        Maximum sum of number in given matrix.
    """
    matrix = []

    for ls in num.split("\n")[1:]:
        matrix.append(ls.split(" "))

    matrix = matrix[:-1]

    return backtrack(matrix, 0, 0)


if __name__ == "__main__":
    NUM = """
3
7 4
2 4 6
8 5 9 3
"""

    print(solver(NUM))
