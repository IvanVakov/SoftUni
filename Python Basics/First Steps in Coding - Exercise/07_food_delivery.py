count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

total_price_chicken = count_chicken_menu * 10.35
total_price_fish = count_fish_menu * 12.40
total_price_vegetarian = count_vegetarian_menu * 8.15

all_menu_price = total_price_vegetarian + total_price_fish + total_price_chicken

sweet = all_menu_price * 0.20

total_price = all_menu_price + sweet + 2.5

print(total_price)