fruit = input()
day = input()
quantity = float(input())
price = 0

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit == 'banana':
        price = quantity * 2.5
    elif fruit == 'apple':
        price = quantity * 1.2
    elif fruit == 'orange':
        price = quantity * 0.85
    elif fruit == 'grapefruit':
        price = quantity * 1.45
    elif fruit == 'kiwi':
        price = quantity * 2.7
    elif fruit == 'pineapple':
        price = quantity * 5.5
    elif fruit == 'grapes':
        price = quantity * 3.85

elif day in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        price = quantity * 2.7
    elif fruit == 'apple':
        price = quantity * 1.25
    elif fruit == 'orange':
        price = quantity * 0.9
    elif fruit == 'grapefruit':
        price = quantity * 1.6
    elif fruit == 'kiwi':
        price = quantity * 3
    elif fruit == 'pineapple':
        price = quantity * 5.6
    elif fruit == 'grapes':
        price = quantity * 4.2

if price == 0.00:
    print('error')
else:
    print(f'{price:.2f}')








