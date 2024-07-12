count = int(input())
student_academy = {}

for _ in range(count):
    student_name = input()
    grades = float(input())

    if student_name not in student_academy:
        student_academy[student_name] = []

    student_academy[student_name].append(grades)

for student, grades in student_academy.items():
    average_grade = sum(grades) / len(grades)
    if average_grade < 4.50:
        continue
    print(f"{student} -> {average_grade:.2f}")