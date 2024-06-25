elements = input().split()
bakery = {}

for word in range(0, len(elements), 2):
    key = elements[word]
    value = elements[word + 1]
    bakery[key] = int(value)

print(bakery)