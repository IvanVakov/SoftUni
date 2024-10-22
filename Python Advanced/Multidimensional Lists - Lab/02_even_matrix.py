rows = int(input())

matrix = []

for _ in range(rows):
    elemets = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(elemets)

print(matrix)