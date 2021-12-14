import re
from collections import defaultdict

recipes = {}
pair_counts = defaultdict(int)

template = input()
for a, b in zip(template[:-1], template[1:]):
    pair_counts[a+b] += 1
input()  # fuck you gabriel


while recipe := input():
    [(adjacent, newchar)] = re.findall("([A-Z]+) -> ([A-Z])", recipe)
    recipes[adjacent] = newchar

for _ in range(40):
    new_count = defaultdict(int)
    for (a, b), count in pair_counts.items():
        if a+b not in recipes:
            new_count[a+b] = count
        else:
            new_letter = recipes[a+b]
            new_count[a+new_letter] += count
            new_count[new_letter+b] += count

    pair_counts = new_count

letter_counts = defaultdict(int)
for pair, pair_count in pair_counts.items():
    for letter in pair:
        letter_counts[letter] += pair_count

# all letters are counter twice except for the first and last
letter_counts[template[0]] += 1
letter_counts[template[-1]] += 1
assert all(v % 2 == 0 for v in letter_counts.values())
letter_counts = {k: v // 2 for k, v in letter_counts.items()}

print(max(letter_counts.values()) - min(letter_counts.values()))
