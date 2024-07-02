words = input().split()
new_dict = {}

for word in words:
    for letter in word:
        if letter in new_dict:
            new_dict[letter] += 1
        else:
            new_dict[letter] = 1

for key, value in new_dict.items():
    print(f"{key} -> {value}")