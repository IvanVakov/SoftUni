count_of_elements = int(input())
unique_compounds = set()

for _ in range(count_of_elements):
    for el in input().split():
        unique_compounds.add(el)

print(*unique_compounds, sep="\n")
