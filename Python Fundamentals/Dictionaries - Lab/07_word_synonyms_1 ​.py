count = int(input())
synonyms = {}

for _ in range(count):
    key = input()
    value = input()

    if key not in synonyms:
        synonyms[key] = []

    synonyms[key].append(value)

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")