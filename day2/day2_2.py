x = 0
y = 0
aim = 0
while inp := input():
    direction, num = inp.split()
    if direction == 'forward':
        x += int(num)
        y += aim*int(num)
    elif direction == 'down':
        aim += int(num)
    elif direction == 'up':
        aim -= int(num)

print(x*y)

