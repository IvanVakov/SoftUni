from math import ceil

numbers = [int(x) for x in input().split(", ")]

groups_count = ceil(max(numbers) / 10)
low_boundary = 1
high_boundary = 10

for index in range(1, groups_count + 1):
    grouped_numbers = [x for x in numbers if low_boundary <= x <= high_boundary]
    print(f"Group of {10 * index}'s: {grouped_numbers}")

    low_boundary += 10
    high_boundary += 10