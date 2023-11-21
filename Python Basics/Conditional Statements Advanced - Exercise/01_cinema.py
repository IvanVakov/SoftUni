project_type = input()
count_rows = int(input())
count_columns = int(input())
income = 0

cinema_capacity = count_columns * count_rows

if project_type == 'Premiere':
    income = cinema_capacity * 12
elif project_type == 'Normal':
    income = cinema_capacity * 7.5
elif project_type == 'Discount':
    income = cinema_capacity * 5

sum_total = project_type * count_rows * count_columns

print(f'{income:.2f} leva')
