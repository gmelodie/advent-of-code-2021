
open_to_close = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def calculate_complete_sequence(line):
    stack = []
    for char in line:
        if char in open_to_close:
            stack.append(open_to_close[char])
        else:
            top = stack.pop(-1)
            if top != char: # fault
                return True, []

    return False, stack[::-1]


def calculate_sequence_score(complete_sequence):
    score = 0
    for closing_char in complete_sequence:
        score = score*5 + points[closing_char]
    return score


valid_scores = []
while line := input():
    is_faulty, complete_sequence = calculate_complete_sequence(line)
    if not is_faulty:
        valid_scores.append(calculate_sequence_score(complete_sequence))

print(sorted(valid_scores)[len(valid_scores)//2])

