import sys

n = int(input())
biggest_num = -sys.maxsize
total_sum = 0

for i in range(1, n + 1):
    current_num = int(input())

    if current_num > biggest_num:
        biggest_num = current_num

    total_sum = total_sum + current_num

all_sum = total_sum - biggest_num

if all_sum == biggest_num:
    print('Yes')
    print(f'Sum = {all_sum}')
else:
    diff = abs(all_sum - biggest_num)
    print('No')
    print(f'Diff = {diff}')