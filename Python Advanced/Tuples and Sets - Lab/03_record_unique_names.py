number = int(input())

unique_names = set()

for _ in range(number):
    names = input()

    if names not in unique_names:
        unique_names.add(names)

print(*unique_names, sep="\n")