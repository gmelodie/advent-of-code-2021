def most_common_bit(matrix, col):
    ones = 0
    zeroes = 0
    for row in range(len(matrix)):
        if matrix[row][col] == '1':
            ones += 1
        else:
            zeroes += 1
    if max(ones, zeroes) == ones:
        return '1'
    return '0'


def least_common_bit(matrix, col):
    if most_common_bit(matrix, col) == '0':
        return '1'
    return '0'


def filter_oxygen(matrix, col):
    filtered = []
    mcb = most_common_bit(matrix, col)
    for row in matrix:
        if row[col] == mcb:
            filtered.append(row)
    return filtered


def filter_co2(matrix, col):
    filtered = []
    lcb = least_common_bit(matrix, col)
    for row in matrix:
        if row[col] == lcb:
            filtered.append(row)
    return filtered


matrix = []
while row := input():
    matrix.append(list(row))

possible_oxygen = matrix.copy()
possible_co2 = matrix.copy()
for col in range(len(matrix[0])):
    if len(possible_oxygen) != 1:
        possible_oxygen = filter_oxygen(possible_oxygen, col)
    if len(possible_co2) != 1:
        possible_co2 = filter_co2(possible_co2, col)

int_oxygen = int("".join(possible_oxygen[0]), 2)
int_co2 = int("".join(possible_co2[0]), 2)
print(int_co2 * int_oxygen)
