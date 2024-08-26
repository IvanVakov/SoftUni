import re

bought_furniture = []
total_price = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
while True:
    line = input()
    if line == "Purchase":
        break
    matches = re.search(pattern, line)

    if matches:
        furniture, price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_price += float(price) * int(quantity)
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")

