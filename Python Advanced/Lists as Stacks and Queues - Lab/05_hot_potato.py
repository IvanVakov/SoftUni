from collections import deque

names = deque(input().split())
rotation = int(input()) - 1

while len(names) > 1:
    names.rotate(-rotation)
    name_to_exit = names.popleft()
    print(f"Removed {name_to_exit}")

print(f"Last is {names.popleft()}")