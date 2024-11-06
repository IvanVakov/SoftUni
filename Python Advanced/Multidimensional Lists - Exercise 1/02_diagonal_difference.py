n = int(input())

matrix= [[int(x) for x in input().split()] for _ in range(n)]
primary = sum([matrix[index][index] for index in range(n)])
secondary = sum([matrix[index][n - index -1] for index in range(n)])

print(abs(primary - secondary))