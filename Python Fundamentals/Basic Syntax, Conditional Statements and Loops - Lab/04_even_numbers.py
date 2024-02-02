number = int(input())

for n in range(1, number+ 1):
    current_number = int(input())

    if not current_number % 2 == 0:
        print(f"{current_number} is odd!" )
        break
else:
    print(f"All numbers are even.")