destination = input()

while destination != 'End':
    minimum_budget = float(input())
    saved_money = 0
    while saved_money < minimum_budget:
       current_money = float(input())
       saved_money += current_money
    print(f"Going to {destination}!")

    destination = input()