team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
teab_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

players = input().split()
game_was_terminated = False

for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in teab_b:
        teab_b.remove(player)

    if len(team_a) < 7 or len(teab_b) < 7:
        game_was_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(teab_b)}")
if game_was_terminated:
    print(f"Game was terminated")
