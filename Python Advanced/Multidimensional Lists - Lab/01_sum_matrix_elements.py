rows, cols = [int(el) for el in input().split(", ")]

matrix = []
for _ in range(rows):
    inner_list = []
    elements_as_string = input().split(", ")
    for num in elements_as_string:
        inner_list.append(int(num))

    matrix.append(inner_list)

sum_of_matrix = 0

for row_idex in range(rows):
    for col_index in range(cols):
        sum_of_matrix += matrix[row_idex][col_index]

print(sum_of_matrix)
print(matrix)