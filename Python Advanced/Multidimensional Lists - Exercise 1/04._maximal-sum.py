rows, cols = tuple(map(int, input().split()))
matrix = [[int(x) for x in input().split()] for row in range(rows)]

max_size = -21
new_matrix = []
total_sum = 0

for row in range(rows -2):
    for col in range(cols -2):
        first_row = matrix[row][col:col+3]
        second_row = matrix[row+1][col:col+3]
        third_row = matrix[row+2][col:col+3]

        total_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if total_sum > max_size:
            max_size = total_sum
            new_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_size}")
for row in range(len(new_matrix)):
    print(*new_matrix[row])
