length_cm = int(input())
width_cm = int(input())
high_cm = int(input())
percent = float(input())


total = length_cm * width_cm * high_cm
volume_liters = total / 1000

all_total = volume_liters * (percent / 100)
liters = volume_liters - all_total

print(liters)