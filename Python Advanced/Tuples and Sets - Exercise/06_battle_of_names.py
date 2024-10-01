number = int(input())
odd_set = set()
even_set = set()

for row in range(1, number + 1):
    names = input()

    ascii_sum_of_name = sum(ord(el) for el in names) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)
    else:
        odd_set.add(ascii_sum_of_name)

if sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*even_set.symmetric_difference(odd_set), sep=', ')