numbers = [float(num) for num in input().split()]

occ = {}

for i in numbers:
    if i not in occ:
        occ[i] = 0
    occ[i] += 1

for key, value in occ.items():
    print(f"{key} - {value} times")
