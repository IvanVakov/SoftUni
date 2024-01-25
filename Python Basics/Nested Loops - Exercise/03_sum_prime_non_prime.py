# 1. въвеждането на цели числа
command = input()  # въведените входни данни -> "stop" или число под формата на текст ("4")

# повтаряме: въвеждаме
# стоп: command == "stop"
# продължавам: command != "stop"

sum_prime = 0  # сума на простите числа
sum_non_prime = 0  # сума на непростите числа

while command != "stop":
    # command = "5" (число под формата на текст)
    number = int(command)  # въведеното число

    if number < 0:
        print('Number is negative.')
        command = input()
        continue

    # проверка дали number е просто или съставно
    # прости числа -> 2 делителя -> самото число и 1
    # съставни числа (непрости) -> повече от 2 делителя
    count = 0  # брой на делителите
    for n in range(1, number + 1):
        if number % n == 0:
            # number може да се раздели на n без остатък -> n ми е делител на number
            count += 1

    # знам брой на делителите на number
    if count == 2:
        # просто число
        sum_prime += number
    else:
        # съставно (непросто)
        sum_non_prime += number

    command = input()  # въвеждам нови данни

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")