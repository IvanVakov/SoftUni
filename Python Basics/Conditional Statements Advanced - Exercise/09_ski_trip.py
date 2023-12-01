days_stay = int(input())
place_for_stay = input()
rating = input()
nights = days_stay - 1
price = 0


if place_for_stay == 'room for one person':
    price = nights * 18
elif place_for_stay == 'apartment':
    price = nights * 25
    if days_stay < 10:
        price = price * 0.7
    elif days_stay >= 10 and days_stay <= 15:
        price = price * 0.65
    elif days_stay >= 15:
        price = price * 0.5
elif place_for_stay == 'president apartment':
    price = nights * 35
    if days_stay< 10:
        price = price * 0.9
    elif days_stay >= 10 and days_stay <= 15:
        price = price * 0.85
    elif days_stay >= 15:
        price = price * 0.8

if rating == 'positive':
    price = price * 1.25
else:
    price = price * 0.9

print(f'{price:.2f}')