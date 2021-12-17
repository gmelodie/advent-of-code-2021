
open_to_close = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def calculate_error(line):
    stack = []
    for char in line:
        if char in open_to_close:
            stack.append(open_to_close[char])
        else:
            top = stack.pop(-1)
            if top != char: # fault
                print(f"expected {top} found {char}")
                return points[char]

    print("returning zero (no faults)")
    return 0


sum_errors = 0
while line := input():
    sum_errors += calculate_error(line)
print(sum_errors)
