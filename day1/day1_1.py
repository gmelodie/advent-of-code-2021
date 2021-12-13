greater = 0
last = int(input())

while inp := input():
    current = int(inp)
    if current > last:
        greater += 1
    last = current

print(greater)

