import re
from collections import defaultdict

graph = defaultdict(list)
need_to_visit = set()

def explore(src_cave: str, path: str, visited: set):
    if src_cave.islower():
        visited.add(src_cave)

    if src_cave == 'end':
        print(path)
        # if len(need_to_visit) == len(visited):
        #     return 1
        return 1

    paths = 0
    for adjacent in graph[src_cave]:
        if adjacent in visited: # visit all ajd caves if not visited
            continue
        paths += explore(adjacent, path + "->" + adjacent, visited.copy())

    return paths


while inp := input():
    [(cave_a, cave_b)] = re.findall("(\w+)-(\w+)", inp)
    graph[cave_a].append(cave_b)
    graph[cave_b].append(cave_a)

    if cave_a.islower():
        need_to_visit.add(cave_a)
    if cave_b.islower():
        need_to_visit.add(cave_b)

print(explore('start', "start", set()))
