greater = 0

one = int(input())
two = int(input())
three = int(input())

while inp := input():
    current = int(inp)
    last_sum = one + two + three
    current_sum = two + three + current
    if current_sum > last_sum:
        greater += 1
    one = two
    two = three
    three = current

print(greater)

