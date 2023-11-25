budget = int(input())
season = input()
count_fishermen = int(input())
price_rent_ship = 0

if season == 'Spring':
    price_rent_ship = 3000
elif season == 'Summer' or season == 'Autumn':
    price_rent_ship = 4200
elif season == 'Winter':
    price_rent_ship = 2600

if count_fishermen <= 6:
    price_rent_ship = price_rent_ship * 0.9
elif count_fishermen > 6 and count_fishermen <= 11:
    price_rent_ship = price_rent_ship * 0.85
elif count_fishermen > 11:
    price_rent_ship = price_rent_ship * 0.75

if count_fishermen % 2 == 0 and season != 'Autumn':
    price_rent_ship = price_rent_ship * 0.95

diff = abs(budget - price_rent_ship)

if budget >= price_rent_ship:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


