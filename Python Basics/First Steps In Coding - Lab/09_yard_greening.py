square_meters = float(input())
price_square_meter = 7.61

total_price = square_meters * price_square_meter
price_discount = total_price * 0.18
final_price = total_price - price_discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {price_discount} lv.')