numbers_as_strings = input().split(' ')
min_numbers = []
max_numbers = []
sum_numbers = []

for num in numbers_as_strings:
    min_numbers.append(int(num))
    max_numbers.append(int(num))
    sum_numbers.append(int(num))

print(f"The minimum number is {min(min_numbers)}")
print(f"The maximum number is {max(max_numbers)}")
print(f"The sum number is: {sum(sum_numbers)}")