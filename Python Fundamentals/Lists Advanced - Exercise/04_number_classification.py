def positive(number):
    return [num for num in number if int(num) >= 0]


def negative(number):
    return [num for num in number if int(num) < 0]


def even(number):
    return [num for num in number if int(num) % 2 == 0]


def odd(number):
    return [num for num in number if int(num) % 2 != 0]


current_number = input().split(", ")
print(f"Positive: {', '.join(positive(current_number))}")
print(f"Negative: {', '.join(negative(current_number))}")
print(f"Even: {', '.join(even(current_number))}")
print(f"Odd: {', '.join(odd(current_number))}")
