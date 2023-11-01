time_first = int(input())
second_first = int(input())
third_first = int(input())

all_sum_sec = time_first + second_first + third_first

total_minutes = all_sum_sec // 60
total_seconds = all_sum_sec % 60

if total_seconds < 10:
    print(f'{total_minutes}:0{total_seconds}')
else:
    print(f'{total_minutes}:{total_seconds}')