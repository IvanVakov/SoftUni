nylon_square_m = int(input())
paint_liters = int(input())
thinner_paint = int(input())
hours_work = int(input())

price_nylon = (nylon_square_m + 2) * 1.5
price_paint = (paint_liters * 1.1) * 14.5
price_thinner = thinner_paint * 5
bags = 0.4

all_total = price_thinner + price_paint + price_nylon + bags
price_hour = (all_total * 0.30) * hours_work
total_sum = all_total + price_hour

print(total_sum)