number_list = list(map(int, input().split(', ')))
indices = [num for num in range(len(number_list)) if number_list[num] % 2 == 0]
print(indices)
