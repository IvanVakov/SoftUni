rows = int(input())

flatten = []

for _ in range(rows):
    innet_list = [int(el) for el in input().split(", ")]
    flatten.extend(innet_list)

print(flatten)