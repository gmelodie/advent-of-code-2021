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

matrix = []
line = input()
while line:
    matrix.append([int(num) for num in line])
    line = input()

ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if is_lowest_point(i, j, matrix):
            ans += 1 + matrix[i][j]


print(ans)

