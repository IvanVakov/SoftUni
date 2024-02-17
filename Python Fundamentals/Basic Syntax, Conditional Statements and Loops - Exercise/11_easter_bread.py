budget = float(input())
price_1_kg_flour = float(input())
easter_bred_counter = 0
colored_eggs_counter = 0

price_1_pack_eggs = price_1_kg_flour * 0.75
price_1_litter_milk = price_1_kg_flour * 1.25 / 4
bred = price_1_kg_flour + price_1_pack_eggs + price_1_litter_milk

while budget >= bred:
    budget -= bred
    easter_bred_counter += 1
    colored_eggs_counter += 3
    if easter_bred_counter % 3 == 0:
        colored_eggs_counter -= easter_bred_counter - 2

print(
    f"You made {easter_bred_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
