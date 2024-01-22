floors = int(input())
flats_per_floor = int(input())

flat_number_counter = 0
type_of_flat = ''

for floor in range(floors, 0, -1):
    for a in range(flats_per_floor):
        flat_number = floor * 10 + a

        if floor == floors:
            type_of_flat = f'L{flat_number}'

        elif floor % 2 == 0:
            type_of_flat = f'O{flat_number}'

        elif floor % 2 != 0:
            type_of_flat = f'A{flat_number}'

        print(type_of_flat, end=' ')

    print()
