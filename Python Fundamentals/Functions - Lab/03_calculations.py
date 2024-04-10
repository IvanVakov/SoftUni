def calculations(string, number_1, number_2):
    if operator == 'multiply':
        return number_1 * number_2
    elif operator == 'divide':
        return number_1 // number_2
    elif operator == 'add':
        return number_1 + number_2
    elif operator == 'subtract':
        return number_1 - number_2


operator = input()
first_number = int(input())
second_number = int(input())
print(calculations(operator, first_number, second_number))