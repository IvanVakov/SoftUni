init_points = int(input())
bonus_points = 0

if init_points <= 100:
    bonus_points = 5
elif init_points <= 1000:
    bonus_points = init_points * 0.2
else:
    bonus_points = init_points * 0.1

if init_points % 2 == 0:
    bonus_points = bonus_points + 1
if init_points % 10 == 5:
    bonus_points = bonus_points + 2


print(bonus_points)
print(bonus_points + init_points)