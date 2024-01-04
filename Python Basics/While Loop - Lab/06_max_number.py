import sys

input_line = input()
max_num = -sys.maxsize

while input_line != 'Stop':
    current_num = int(input_line)

    if current_num > max_num:
        max_num = current_num

    input_line = input()
print(max_num)