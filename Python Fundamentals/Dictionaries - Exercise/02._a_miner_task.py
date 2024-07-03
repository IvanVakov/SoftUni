line = input()
money = {}

while line != "stop":
    quantity = int(input())

    if line not in money:
        money[line] = quantity

    else:
        money[line] += quantity

    line = input()

for item, quantity in money.items():
    print(f"{item} -> {quantity}")