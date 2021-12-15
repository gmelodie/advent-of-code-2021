def in_bounds(matrix, i, j):
    rows = len(matrix)
    cols = len(matrix[0])
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return False
    return True

def read_matrix():
    matrix = []
    while row := input():
        matrix.append([int(num) for num in list(row)])
    return matrix


def pretty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

