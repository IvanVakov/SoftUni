n = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    current_num = int(input())
    if i % 2 == 0:
        even_sum = even_sum + current_num
    else:
        odd_sum = odd_sum + current_num
if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {odd_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')


