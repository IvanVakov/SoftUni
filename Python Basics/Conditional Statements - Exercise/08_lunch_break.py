import math

name_serial = input()
episode_duration = int(input())
break_duration = int(input())

time_to_eat = break_duration / 8
time_relax = break_duration / 4

time_left =(break_duration - time_to_eat - time_relax)

diff = abs(time_left - episode_duration)
rounded_diff = math.ceil(diff)

if time_left >= episode_duration:
    print(f"You have enough time to watch {name_serial} and left with {rounded_diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {rounded_diff} more minutes.")

