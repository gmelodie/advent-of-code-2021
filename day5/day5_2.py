import re

MATRIX_LEN = 1000

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='')
        print()


def mark_horizontal_line(matrix, row, x1, x2):
    for i in range(x1, x2+1):
        matrix[row][i] += 1
    return matrix


def mark_vertical_line(matrix, col, y1, y2):
    for i in range(y1, y2+1):
        matrix[i][col] += 1
    return matrix


def mark_diagonal_line(matrix, x1, x2, y1, y2):
    if x1 < x2 and y1 < y2: # x1, y1 is above and to the left
        start_y = y1
        start_x = x1
        end_y = y2
        direction = 1
    elif x1 < x2 and y1 > y2: # x1, y1 is below and to the left
        start_y = y2
        start_x = x2
        end_y = y1
        direction = -1
    elif x1 > x2 and y1 < y2: # x1, y1 is above and to the right
        start_y = y1
        start_x = x1
        end_y = y2
        direction = -1
    elif x1 > x2 and y1 > y2: # x1, y1 is below and to the right
        start_y = y2
        start_x = x2
        end_y = y1
        direction = 1

    delta_col = 0
    for row in range(start_y, end_y+1):
        col = start_x + direction*delta_col
        matrix[row][col] += 1
        delta_col += 1

    return matrix


matrix = []
for i in range(MATRIX_LEN):
    row = [0]*MATRIX_LEN
    matrix.append(row)

while line := input():
    [(x1, y1, x2, y2)] = re.findall("(\d+),(\d+) -> (\d+),(\d+)", line)
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    print(f"marking {y1},{x1} -> {y2},{x2}")
    if y1 == y2: # horizontal line
        matrix = mark_horizontal_line(matrix, y1, min_x, max_x)
    elif x1 == x2:
        matrix = mark_vertical_line(matrix, x1, min_y, max_y)
    else:
        matrix = mark_diagonal_line(matrix, x1, x2, y1, y2)



overlaps = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] >= 2:
            overlaps += 1

print(overlaps)


