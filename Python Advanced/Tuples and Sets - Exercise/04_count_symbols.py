text = input()

count_symbols = {}

for word in text:
    if word not in count_symbols:
        count_symbols[word] = 0

    count_symbols[word] += 1

for word, count in sorted(count_symbols.items()):
    print(f"{word}: {count} time/s")