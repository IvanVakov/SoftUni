rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

sum_diagonal = 0
for index in range(rows):
    sum_diagonal += matrix[index][index]

print(sum_diagonal)