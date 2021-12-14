from collections import Counter
import re

# ABC
# AZBBXCjjj
def relax_polymer(polymer, recipes): # eh um step
    new_polymer = ""
    for a, b in zip(polymer[:-1], polymer[1:]):
        new_polymer += a + recipes.get(a+b, "")
    return new_polymer + polymer[-1]


template = input()
input() # fuck you bruno
recipes = {}
while recipe := input():
    [(adjacent, newchar)] = re.findall("([A-Z]+) -> ([A-Z])", recipe)
    recipes[adjacent] = newchar

for i in range(10):
    print("Step", i)
    template = relax_polymer(template, recipes)

c = [v for k,v in Counter(template).items()]
print(max(c) - min(c))

