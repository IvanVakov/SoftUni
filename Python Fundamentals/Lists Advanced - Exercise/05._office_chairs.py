number_of_rooms = int(input())
free_chairs = 0
game_on = True

for room in range(1, number_of_rooms + 1):
    next_line = input().split()
    chairs = next_line[0]
    visitors = int(next_line[1])

    if visitors > len(chairs):
        needed_chairs = visitors - len(chairs)
        print(f"{needed_chairs} more chairs needed in room {room}")
        game_on = False
    else:
        difference = abs(len(chairs) - visitors)
        free_chairs += difference

if game_on:
    print(f"Game On, {free_chairs} free chairs left")
