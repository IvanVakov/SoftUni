count_jury = int(input())  # бр. журито = бр. оценки за всяка презентация
# повтаряме: въвеждаме презентации
# стоп: входни данни == "Finish"
# продължаваме: входни данни != "Finish"

sum_all_grades = 0  # сума от оценките за всички презентации
count_all_grades = 0  # брой на всички оценки за всички презентации

presentation = input()  # име на презентация или "Finish"
while presentation != "Finish":
    # presentation -> име на презентация
    # 1. получа оценки от журито
    sum_grades_per_presentation = 0  # сума от оценките на журито за презентацията
    for jury in range(1, count_jury + 1):
        grade = float(input())
        count_all_grades += 1
        sum_grades_per_presentation += grade
        sum_all_grades += grade
    # 2. print
    average_grade_per_presentation = sum_grades_per_presentation / count_jury
    print(f"{presentation} - {average_grade_per_presentation:.2f}.")

    presentation = input()

average_grade_all_presentations = sum_all_grades / count_all_grades
print(f"Student's final assessment is {average_grade_all_presentations:.2f}.")