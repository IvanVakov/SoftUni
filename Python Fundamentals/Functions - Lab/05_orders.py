def orders(product, total_quantity):
    if product == 'coffee':
        price = 1.5 * total_quantity
        return f'{price:.2f}'

    elif product == 'water':
        price = 1 * total_quantity
        return f'{price:.2f}'

    elif product == 'coke':
        price = 1.4 * total_quantity
        return f'{price:.2f}'

    elif product == 'snacks':
        price = 2 * total_quantity
        return f'{price:.2f}'


product_name = input()
quantity = float(input())
print(orders(product_name, quantity))