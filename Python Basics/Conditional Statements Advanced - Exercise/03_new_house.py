type_flowers = input()
count_flowers = int(input())
budget = int(input())
price_leva = 0

if type_flowers == 'Roses':
    price_leva = count_flowers * 5
elif type_flowers == 'Dahlias':
    price_leva = count_flowers * 3.8
elif type_flowers == 'Tulips':
    price_leva = count_flowers * 2.8
elif type_flowers == 'Narcissus':
    price_leva = count_flowers * 3
elif type_flowers == 'Gladiolus':
    price_leva = count_flowers * 2.5

if type_flowers == 'Roses' and count_flowers > 80:
    price_leva = price_leva * 0.9
elif type_flowers == 'Dahlias' and count_flowers > 90:
    price_leva = price_leva * 0.85
elif type_flowers == 'Tulips' and count_flowers > 80:
    price_leva = price_leva * 0.85
elif type_flowers == 'Narcissus' and count_flowers < 120:
    price_leva = price_leva * 1.15
elif type_flowers == 'Gladiolus' and count_flowers < 80:
    price_leva = price_leva * 1.2

diff = abs(budget - price_leva)
if budget >= price_leva:
    print(f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

