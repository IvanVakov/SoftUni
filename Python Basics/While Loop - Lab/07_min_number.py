import sys

input_line = input()
min_num = sys.maxsize

while input_line != 'Stop':
    current_num = int(input_line)

    if current_num < min_num:
        min_num = current_num

    input_line = input()

print(min_num)