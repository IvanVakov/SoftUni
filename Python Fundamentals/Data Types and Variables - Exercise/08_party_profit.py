companions = int(input())
days_adventure = int(input())
coins = 0

for day in range(1, days_adventure + 1):

    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5

    if day % 3 == 0:
        coins -= 3 * companions
    if day % 5 == 0:
        coins += 20 * companions
        if day % 3 == 0:
            coins -= 2 * companions
    coins += 50
    coins -= 2 * companions
coins_per_companion = int(coins // companions)

print(f"{companions} companions received {coins_per_companion} coins each.")