number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    name, grades = tuple(input().split())
    grades = float(grades)

    if name not in students:
        students[name] = []

    students[name].append(grades)


for name, grade in students.items():
    avg = sum(grade) / len(grade)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grade])} (avg: {avg:.2f})")