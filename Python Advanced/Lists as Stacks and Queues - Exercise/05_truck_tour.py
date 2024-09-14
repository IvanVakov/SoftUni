from collections import deque

number_of_petrols = int(input())
pums = deque([[int(x) for x in input().split()] for _ in range(number_of_petrols)])

pums_copy = pums.copy()

gas_in_car = 0
index = 0

while pums_copy:
    petrol, km = pums_copy.popleft()
    gas_in_car += petrol

    if gas_in_car >= km:
        gas_in_car -= km

    else:
        pums.rotate(-1)
        gas_in_car = 0
        pums_copy = pums.copy()
        index += 1

print(index)


