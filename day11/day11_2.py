def pretty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

def in_bounds(matrix, i, j):
    rows = len(matrix)
    cols = len(matrix[0])
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return False
    return True


def update_item(matrix, i, j):
    if not in_bounds(matrix, i, j):
        return
    if matrix[i][j] == 0: # already flashed
        return
    matrix[i][j] += 1
    if matrix[i][j] <= 9:
        return

    # Flash
    matrix[i][j] = 0

    adjacent = [(1,1), (1,0), (0,1), (-1,-1), (-1, 0), (0, -1), (1, -1), (-1, 1)]
    for (sum_i, sum_j) in adjacent:
        update_item(matrix, i+sum_i, j+sum_j)


def step_once(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1
    # pretty_print(matrix)
    # print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 9:
                update_item(matrix, i, j)
                # pretty_print(matrix)
                # print()

def count_flashes(matrix):
    flashes = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                flashes += 1
    return flashes


matrix = []
while row := input():
    matrix.append([int(num) for num in row])

rows = len(matrix)
cols = len(matrix[0])
iteration = 0
while True:
    iteration += 1
    step_once(matrix)
    if count_flashes(matrix) == rows*cols:
        break

print(iteration)

