budget_movie = float(input())
count_statists = int(input())
price_shirts_statists = float(input())

set_movie = budget_movie * 0.1
price_clouts = count_statists * price_shirts_statists

if count_statists > 150:
    price_clouts = price_clouts * 0.9

total_amount = set_movie + price_clouts

diff = abs(budget_movie - total_amount)

if budget_movie >= total_amount:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")


