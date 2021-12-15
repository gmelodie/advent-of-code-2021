

matrix = []
while row := input():
    matrix.append(list(row))

gamma_rate = ''
epsilon_rate = ''

for col in range(len(matrix[0])):
    ones = 0
    zeroes = 0
    for row in range(len(matrix)):
        if matrix[row][col] == '1':
            ones += 1
        else:
            zeroes += 1
    if max(ones, zeroes) == zeroes:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'


int_gamma_rate = int(gamma_rate, 2)
int_epsilon_rate = int(epsilon_rate, 2)
print(int_gamma_rate * int_epsilon_rate)
