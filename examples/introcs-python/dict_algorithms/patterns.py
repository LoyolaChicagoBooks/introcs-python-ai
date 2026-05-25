# start: counting
words = ["apple", "banana", "apple", "pear", "banana", "apple"]
counts = {}

for w in words:
    if w not in counts:
        counts[w] = 1
    else:
        counts[w] += 1

print(counts)
# end: counting


# start: filtering
scores = {"Alice": 95, "Bob": 82, "Carol": 71, "Diana": 99}
high_scores = {}

for name, score in scores.items():
    if score > 80:
        high_scores[name] = score

print(high_scores)
# end: filtering


# start: grouping
words = ["apple", "ant", "banana", "berry", "car", "cat"]
groups = {}

for w in words:
    first = w[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(w)

print(groups)
# end: grouping


# start: list_of_dicts
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Cara", "age": 30},
]

freq = {}
for p in people:
    age = p["age"]
    freq[age] = freq.get(age, 0) + 1

print(freq)
# end: list_of_dicts


# start: group_by_length
def group_by_length(words):
    groups = {}
    for w in words:
        groups.setdefault(len(w), []).append(w)
    return groups


print(group_by_length(["tea", "to", "apple", "jam", "bag"]))
# end: group_by_length
