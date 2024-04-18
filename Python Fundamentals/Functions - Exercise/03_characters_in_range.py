def character_in_range (input1, input2):
    characters = []
    for current_char in range (ord(input1) + 1, ord(input2)):
        characters.append(chr(current_char))
    return characters

first_string = input()
second_string = input()
result = character_in_range(first_string, second_string)
print(*result)