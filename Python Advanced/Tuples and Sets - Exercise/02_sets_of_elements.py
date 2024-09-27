n, m = [int(num) for num in input().split()]

first_set = {int(input()) for num in range(n)}
second_set = {int(input()) for num in range(m)}

intersection = first_set.intersection(second_set)

print(*intersection, sep="\n")
