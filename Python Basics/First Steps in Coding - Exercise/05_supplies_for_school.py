count_packets_pens = int(input())
count_packets_markers = int(input())
liters_supply_cleaning = int(input())
percent_discount = int(input())

price_pens = 5.8
price_markers = 7.2
price_supply = 1.2

total_sum_pens = count_packets_pens * price_pens
total_sum_markers = count_packets_markers * price_markers
total_sum_supply = liters_supply_cleaning * price_supply

total_sum = total_sum_supply + total_sum_markers + total_sum_pens
discount_sum = total_sum * (percent_discount / 100)
needed_sum = total_sum - discount_sum

print(needed_sum)