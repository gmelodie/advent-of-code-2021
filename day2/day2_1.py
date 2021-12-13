x = 0
y = 0
while inp := input():
    direction, num = inp.split()
    if direction == 'forward':
        x += int(num)
    elif direction == 'down':
        y += int(num)
    elif direction == 'up':
        y -= int(num)

print(x*y)

