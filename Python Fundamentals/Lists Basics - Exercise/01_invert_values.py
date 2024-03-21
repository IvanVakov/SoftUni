string = input().split()
opposite_numbers = []

for current_string in string:
    opposite_numbers.append(-int(current_string))

print(opposite_numbers)