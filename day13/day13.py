import numpy as np
MAX = 10000

matrix = np.full((MAX, MAX), False)


def pretty_print(matrix):
    print_matrix = np.full(matrix.shape, ".")
    print_matrix[matrix] = "#"
    for row in print_matrix:
        for symb in row:
            print(symb, end="")
        print()


def fold_once(matrix, axis, value):
    if axis == "y":  # top fold
        matrix = matrix.T

    assert matrix[:, value].sum() == 0

    iter = matrix.shape[1] - value
    for i in range(iter):
        matrix[:, value-i] = np.logical_or(matrix[:, value-i], matrix[:, value+i])

    matrix = matrix[:, :value]
    return matrix if axis == "x" else matrix.T

max_x, max_y = float("-inf"), float("-inf")

while inp := input():  # walrus
    y, x = [int(num) for num in inp.split(",")]
    matrix[x, y] = True
    max_x = max(x, max_x)
    max_y = max(y, max_y)

if max_x % 2 != 0:
    max_x += 1
if max_y % 2 != 0:
    max_y += 1

first = False
matrix = matrix[:max_x+1, :max_y+1]

while inp := input():
    axis, value = inp.split(" ")[-1].split("=")
    value = int(value)
    matrix = fold_once(matrix, axis, value)

    if not first:
        print("Part 1:", matrix.sum())
        first = True

print()
print("PART 2")
print("======")
pretty_print(matrix)
