from collections import deque

clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
rack_counter = 1
current_rack_space = rack_capacity

while clothes:
    dress = clothes.pop()

    if current_rack_space >= dress:
        current_rack_space -= dress

    else:
        rack_counter += 1
        current_rack_space = rack_capacity - dress

print(rack_counter)



