open_tabs = int(input())
salary = int(input())

for i in range(1, open_tabs + 1):
    tab = input()
    if tab == 'Facebook':
        salary = salary - 150
    elif tab == 'Instagram':
        salary = salary - 100
    elif tab == 'Reddit':
        salary = salary - 50

    if salary <= 0:
        break

if salary <= 0:
    print(f'You have lost your salary.')
else:
    print(f'{salary}')