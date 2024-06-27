products = {}
line = input()

while line != "statistics":
    tokes = line.split(": ")
    product = tokes[0]
    quantity = int(tokes[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity

    line = input()

print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")