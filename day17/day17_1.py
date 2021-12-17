import re
import math

# might be useful for part 2
def find_pos(initial_x_velocity, initial_y_velocity, step_n):
    t = step_n
    y_pos = initial_y_velocity*t - (t*t-t)/2

    if t >= initial_x_velocity: # stopped
        t = initial_x_velocity # pos in t will remain that since v is 0

    if initial_x_velocity < 0: # acceleration positive (against movement)
        x_pos = initial_x_velocity*t + (t*t-t)/2
    else:
        x_pos = initial_x_velocity*t - (t*t-t)/2

    return x_pos, y_pos


def in_target(cur_x, cur_y):
    global x0, xn, y0, yn
    # print(x0, xn, y0, yn)
    # print(cur_x, cur_y)
    if x0 <= cur_x and cur_x <= xn and y0 <= cur_y and cur_y <= yn:
        return True
    return False


def step_through(vx, vy):
    global yn, xn
    step = 1
    highest_y = 0
    cur_x, cur_y = find_pos(vx, vy, step)
    while cur_y >= y0 and cur_x <= xn:
        if cur_y > highest_y:
            highest_y = cur_y
        if in_target(cur_x, cur_y):
            return True, highest_y, (cur_x, cur_y)
        step += 1
        cur_x, cur_y = find_pos(vx, vy, step)
    return False, 0, ()


line = input()
[(x0, xn, y0, yn)] = re.findall("target area: x=(-?\d+)\.\.(-?\d+)\,\ y=(-?\d+)\.\.(-?\d+)", line)
x0 = int(x0)
xn = int(xn)
y0 = int(y0)
yn = int(yn)

# t = vx (position stops when velocity reaches 0, which is after vx steps)
# s = s0 + vx*t + at**2/2 (if t = vx)
# s = vx**2/2
# x0 <= vx**2/2 <= xn
# sqrt(2*x0) <= vx <= sqrt(2*xn)

start_vx = int(math.sqrt(2*x0))-1
end_vx = int(math.sqrt(2*xn))+1

print(start_vx, end_vx)
for vx in range(start_vx, end_vx+1):
    for angle in range(89, 0, -1):
        vy = int(math.tan(angle*math.pi/180)*vx)+1
        if vy == 0:
            continue
        print(vx, vy)
        is_path, highest_y, intercept_pos = step_through(vx, vy)
        if is_path:
            print('found!', vx, vy, 'in pos', intercept_pos)
            break
    if is_path:
        break

print(highest_y)

