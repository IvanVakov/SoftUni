from collections import deque

quantity_food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for food in orders.copy():
    if quantity_food >= food:
        orders.popleft()
        quantity_food -= food

    else:
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break

else:
    print("Orders complete")