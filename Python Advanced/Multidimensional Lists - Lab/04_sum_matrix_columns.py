row, cow = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(row):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

for cow_index in range(cow):
    sum_of_coll_elements = 0
    for row_index in range(row):
        sum_of_coll_elements += matrix[row_index][cow_index]

    print(sum_of_coll_elements)
