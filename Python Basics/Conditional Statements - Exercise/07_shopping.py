budget_Petur = float(input())
count_video_cards = int(input())
count_procesors = int(input())
count_ram = int(input())

amount__video_cards = count_video_cards * 250
price_procesors = amount__video_cards * 0.35
amount_procesors = count_procesors * price_procesors
price_ram = amount__video_cards * 0.10
amount_ram = count_ram * price_ram

total_price = amount__video_cards + amount_procesors + amount_ram

if count_video_cards > count_procesors:
    total_price = total_price - (total_price * 0.15)

if total_price <= budget_Petur:
    price_left = (budget_Petur - total_price)
    print(f"You have {price_left:.2f} leva left!")
else:
     diff = abs(total_price - budget_Petur)
     print(f"Not enough money! You need {diff:.2f} leva more!")