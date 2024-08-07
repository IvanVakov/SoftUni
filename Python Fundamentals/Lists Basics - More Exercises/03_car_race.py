# 02. Car Race
race = [int(i) for i in input().split(' ')]
finish = len(race) // 2
f_car = race[0:finish]
s_car = race[-1:finish:-1]

score_f_car = 0
score_s_car = 0

for i in f_car:
    score_f_car += i
    if i == 0:
        score_f_car *= 0.8

for y in s_car:
    score_s_car += y
    if y == 0:
        score_s_car *= 0.8

if score_f_car > score_s_car:
    print(f"The winner is right with total time: {score_s_car:.1f}")
else:
    print(f"The winner is left with total time: {score_f_car:.1f}")