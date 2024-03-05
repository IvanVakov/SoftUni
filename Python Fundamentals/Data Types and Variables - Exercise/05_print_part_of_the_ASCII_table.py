first_character = int(input())
last_character = int(input())

for line in range(first_character, last_character + 1):
    line = chr(line)

    print(line, end=' ')