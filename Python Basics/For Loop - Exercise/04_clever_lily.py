lili_age = int(input())
wash_machine_price = float(input())
toy_price = int(input())
brother = 0
money = 0
toys = 0
total_sum = 0

for i in range(1, lili_age + 1):
    if i % 2 == 0:
        money = money + 10
        brother = brother + 1
        total_sum = total_sum + money
    else:
        toys = toys + 1

all_sum = (toy_price * toys) + total_sum - brother


diff = abs(all_sum - wash_machine_price)
if all_sum >= wash_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')