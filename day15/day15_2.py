import time
from collections import defaultdict

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

def read_matrix():
    matrix = []
    while row := input():
        matrix.append([int(num) for num in list(row)])
    return matrix


def gen_number(n, original_number):
    new_number = original_number
    for _ in range(n):
        new_number += 1
        if new_number == 10:
            new_number = 1
    return new_number


def expand_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    expanded_matrix = []
    for i in range(rows*5):
        expanded_matrix.append([])
        for j in range(cols*5):
            n = i//rows + j//cols
            original_number = matrix[i%rows][j%cols]
            expanded_matrix[i].append(gen_number(n, original_number))
    return expanded_matrix



adjacent = [(1,0), (0,1), (-1, 0), (0, -1)]
matrix = expand_matrix(read_matrix())
# pretty_print(matrix)
rows = len(matrix)
cols = len(matrix[0])
end = (rows-1, cols-1)
scores = []
risks = []
for i in range(rows):
    scores.append([])
    risks.append([])
    for j in range(cols):
        scores[i].append(float('inf'))
        risks[i].append(float('inf'))


def distance_from_end(pos):
    return rows - pos[0] + cols - pos[1]


def calculate_score(pos):
    return risks[pos[0]][pos[1]] + distance_from_end(pos)


def reconstruct_path(came_from, pos):
    if pos == (0,0):
        return [(0,0)]
    if pos not in came_from:
        print(f"Error! Can't find previous position for {pos}")
        return []
    return [p for p in reconstruct_path(came_from, came_from[pos])] + [pos]


def find_lowest_score(scores, open_to_look):
    lowest_score = float("inf")
    lowest_score_pos = (0,0)
    for pos in open_to_look:
        if scores[pos[0]][pos[1]] < lowest_score:
            lowest_score = scores[pos[0]][pos[1]]
            lowest_score_pos = pos
    return lowest_score_pos



risks[0][0] = 1
scores[0][0] = calculate_score((0,0))
open_to_look = set()
open_to_look.add((0,0))
came_from = {}

print("This may take a minute or so")
while len(open_to_look) != 0:
    current = find_lowest_score(scores, open_to_look)
    # print(current, " -> ", end="")
    # time.sleep(3)

    if current == end:
        print(f"Found path! Total risk is {risks[end[0]][end[1]] - 1}")
        print(f"Path is too big to reconstruct recursively")
        # print(reconstruct_path(came_from, end))
        break

    open_to_look.remove(current)
    i = current[0]
    j = current[1]
    for (sum_i, sum_j) in adjacent:
        if not in_bounds(matrix, i+sum_i, j+sum_j):
            continue

        tentative_risk = matrix[i+sum_i][j+sum_j] + risks[i][j]
        if tentative_risk < risks[i+sum_i][j+sum_j]:
            risks[i+sum_i][j+sum_j] = tentative_risk
            scores[i+sum_i][j+sum_j] = calculate_score((i+sum_i, j+sum_j))
            came_from[(i+sum_i, j+sum_j)] = (i, j)
            if (i+sum_i, j+sum_j) not in open_to_look:
                open_to_look.add((i+sum_i, j+sum_j))

    # print(open_to_look)

