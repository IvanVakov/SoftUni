text = input()
all_sum = 0

for i in text:
    if i == 'a':
        all_sum += 1
    elif i == 'e':
        all_sum += 2
    elif i == 'i':
        all_sum += 3
    elif i == 'o':
        all_sum += 4
    elif i == 'u':
        all_sum += 5

print(all_sum)

