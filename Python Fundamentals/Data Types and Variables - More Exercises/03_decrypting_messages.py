key = int(input())
number_of_lines = int(input())
message = ''
combination = ''

for iteraion in range(number_of_lines):
    letter = input()

    combination = key + ord(letter)
    combination = chr(combination)
    message += combination

print(message)