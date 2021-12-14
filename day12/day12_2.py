import re
from collections import defaultdict

graph = defaultdict(list)
need_to_visit = set()

def explore(src_cave: str, path: str, visited: set, visited_small_twice):
    if src_cave.islower():
        visited.add(src_cave)

    if src_cave == 'end':
        print(path)
        # if len(need_to_visit) == len(visited):
        #     return 1
        return 1

    paths = 0
    for adjacent in graph[src_cave]:
        # visit all ajd caves if not visited (can visit one twice)
        if adjacent in visited:
            if not visited_small_twice and adjacent != 'end' and adjacent != 'start':
                paths += explore(adjacent, path + "->" + adjacent, visited.copy(), True)
            continue
        paths += explore(adjacent, path + "->" + adjacent, visited.copy(), visited_small_twice)

    return paths


while inp := input():
    [(cave_a, cave_b)] = re.findall("(\w+)-(\w+)", inp)
    graph[cave_a].append(cave_b)
    graph[cave_b].append(cave_a)

    if cave_a.islower():
        need_to_visit.add(cave_a)
    if cave_b.islower():
        need_to_visit.add(cave_b)

print(explore('start', "start", set(), False))
