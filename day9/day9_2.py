def is_lowest_point(i, j, matrix):
    valid_neighs = []
    if i-1 >= 0:
        valid_neighs.append(matrix[i-1][j])
    if i+1 < len(matrix):
        valid_neighs.append(matrix[i+1][j])
    if j-1 >= 0:
        valid_neighs.append(matrix[i][j-1])
    if j+1 < len(matrix[i]):
        valid_neighs.append(matrix[i][j+1])

    return all(matrix[i][j] < x for x in valid_neighs)


def paint_basin(matrix, i, j):
    if i < 0 or i >= len(matrix):
        return 0
    if j < 0 or j >= len(matrix[i]):
        return 0
    if matrix[i][j] == 9:
        return 0
    matrix[i][j] = 9
    return 1 + paint_basin(matrix, i+1, j) \
        + paint_basin(matrix, i-1, j) \
        + paint_basin(matrix, i, j+1) \
        + paint_basin(matrix, i, j-1) \


matrix = []
line = input()
while line:
    matrix.append([int(num) for num in line])
    line = input()

all_basins = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if is_lowest_point(i, j, matrix):
            all_basins.append(paint_basin(matrix, i, j))

all_basins = sorted(all_basins)
print(all_basins[-1]*all_basins[-2]*all_basins[-3])

