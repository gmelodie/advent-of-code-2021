import math


root = None


def find_next_left(node):
    # First go up
    cur = node
    while cur.parent is not None:
        if cur.parent.left != cur:
            cur = cur.parent.left
            break
        cur = cur.parent

    if cur.parent == None:
        return None

    # Then find leftmost child below cur
    while cur.value is None:
        cur = cur.right

    return cur


def find_next_right(node):
    # First go up
    cur = node
    while cur.parent is not None:
        if cur.parent.right != cur:
            cur = cur.parent.right
            break
        cur = cur.parent

    if cur.parent == None:
        return None

    # Then find leftmost child below cur
    while cur.value is None:
        cur = cur.left

    return cur


class SnailNumber():
    def __init__(self, left=None, right=None, value=None, \
                 parent=None, nesting_level=0):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.nesting_level = nesting_level

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        # return f"[{self.left.__str__()},{self.right.__str__()}] ({self.nesting_level})"
        return f"[{self.left.__str__()},{self.right.__str__()}]"

    def explode(self):
        print(f'exploding {self}')
        assert self.value is None
        assert self.left is not None
        assert self.left.value is not None
        assert self.right is not None
        assert self.right.value is not None

        node_left = find_next_left(self)
        node_right = find_next_right(self)
        if node_left is not None:
            node_left.value += self.left.value
        if node_right is not None:
            node_right.value += self.right.value

        self.left = None
        self.right = None
        self.value = 0

    def split(self):
        print(f'splitting {self}')
        assert self.value is not None
        assert self.left is None
        assert self.right is None
        self.left = SnailNumber(parent=self, \
                                nesting_level=self.nesting_level+1, \
                                value=math.floor(self.value/2))
        self.right = SnailNumber(parent=self, \
                                nesting_level=self.nesting_level+1, \
                                value=math.ceil(self.value/2))
        self.value = None

    def reduce_once(self):
        global root
        # print(f'reducing {self} (val: {self.value}, left: {self.left}, right: {self.right})')
        if self.value is None: # first we reduce children
            assert self.left is not None
            assert self.right is not None
            if self.nesting_level >= 4 and self.left.value != None and self.right.value != None:
                self.explode()
                print(f'after explode: {root}')
                return True

            if self.right.value is None and self.left.value is not None:
                stop = self.right.reduce_once()
                if stop:
                    return True
                stop = self.left.reduce_once()
                if stop:
                    return True
            else:
                stop = self.left.reduce_once()
                if stop:
                    return True
                stop = self.right.reduce_once()
                if stop:
                    return True
        elif self.value >= 10:# raw number >= 10
            self.split()
            print(f'after split: {root}')
            return True
        return False

    def magnitude(self):
        if self.value is not None:
            return self.value
        return 3*self.left.magnitude() + 2*self.right.magnitude()


def snail_add(number_a, number_b):
    global root
    stack = [number_a, number_b]

    # update nesting level information
    while len(stack) != 0:
        cur = stack.pop()
        cur.nesting_level+=1
        if cur.left is not None:
            stack.append(cur.left)
        if cur.right is not None:
            stack.append(cur.right)

    root = SnailNumber(left=number_a, right=number_b)
    number_b.parent = root
    number_a.parent = root

    continue_reducing = root.reduce_once()
    while continue_reducing:
        continue_reducing = root.reduce_once()
    return root


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
def read_snail_number(line, parent=None, nesting_level=0):
    if not line.startswith('['): # raw number
        return SnailNumber(value=int(line), parent=parent, nesting_level=nesting_level)

    line = line[1:-1] # strip surrounding [ and ]

    left, right = split_line(line)

    number = SnailNumber()
    number.parent = parent
    number.nesting_level = nesting_level
    number.left = read_snail_number(left, parent=number, nesting_level=nesting_level+1)
    number.right = read_snail_number(right, parent=number, nesting_level=nesting_level+1)

    return number


line = input()
sum_numbers = read_snail_number(line)
while line := input():
    number = read_snail_number(line)
    print(f'{sum_numbers}')
    print(f"+ {number}")
    sum_numbers = snail_add(sum_numbers, number) # add already reduces
    print(f'= {sum_numbers}')

print(sum_numbers.magnitude())


