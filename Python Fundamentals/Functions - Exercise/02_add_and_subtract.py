def sum_numbers(number1, number2):
    return number1 + number2


def subtract(sum, number3):
    return sum - number3


def add_and_subtract(number1, number2, number3):
    sum_of_number1_and_number2 = sum_numbers(number1, number2)
    result = subtract(sum_of_number1_and_number2, number3)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))

