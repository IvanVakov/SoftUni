number_of_lines = int(input())
water_tank = 255
total_liters = 0

for liters in range(1, number_of_lines + 1):
    liters_of_water = int(input())

    if water_tank - liters_of_water < 0:
        print(f"Insufficient capacity!")
        continue
    total_liters += liters_of_water
    water_tank -= liters_of_water

print(total_liters)