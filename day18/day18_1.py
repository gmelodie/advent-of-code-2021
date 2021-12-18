
LEFT = 0
RIGHT = 1


def magnitude(number):
    if isinstance(number, int):
        return number
    return 3*magnitude(number[LEFT]) + 2*magnitude(number[RIGHT])


def split_line(line): # line doesn't have surrounding [ and ]
    nest = 0
    for i, char in enumerate(list(line)):
        if char == '[':
            nest += 1
        elif char == ']':
            nest -= 1

        elif char == ',' and nest == 0:
            return line[:i], line[i+1:]

    print(f'error! invalid split line: {line}')
    return line


# [[1,1],2]
def read_snail_number(line):
    if not line.startswith('['): # raw number
        return int(line)
    line = line[1:-1] # strip surrounding [ and ]
    left, right = split_line(line)
    return [read_snail_number(left), read_snail_number(right)]


def explode(pair):
    if isinstance(pair, int):
        print(f'oops, trying to explode a regular number! {pair}')
        exit(1)



def reduce_snail(number, nesting_level=0):
    if isinstance(number ,int) and number < 10: # reg number < 10
        return number

    if nesting_level == 4:
        number[LEFT] = explode(number[LEFT])
    elif isinstance(number, int) and number >= 10: # is regular number >= 10
        number = split(number)

    number[LEFT] = reduce_snail(number[LEFT], nesting_level+1)
    number[RIGHT] = reduce_snail(number[RIGHT], nesting_level+1)

    return number


# sum_numbers = input()
while line := input():
    number = read_snail_number(line)
    print(number)
    # sum_numbers = add_snail(sum_numbers, number)

# print(calculate_magnitude(sum_numbers))


