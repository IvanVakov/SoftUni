trip_price = float(input())
count_puzzle = int(input())
count_dolls = int(input())
count_teddy_bear = int(input())
count_minions = int(input())
count_truck = int(input())

total_sum = (count_puzzle * 2.6) + (count_dolls * 3) + (count_teddy_bear * 4.1) + (count_minions * 8.2) + (count_truck * 2)
toys_count = count_puzzle + count_dolls + count_teddy_bear + count_minions + count_truck

if toys_count >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.1)
diff = abs(trip_price - total_sum)


if total_sum >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")