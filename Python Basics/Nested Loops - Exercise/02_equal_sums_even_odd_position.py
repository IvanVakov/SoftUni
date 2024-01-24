first_number = int(input())
second_number = int(input())

for f in range(first_number, second_number + 1):

    hundred_thousands = f // 100000
    ten_thousands = (f // 10000) % 10
    thousand = (f // 1000) % 10
    hundreds = (f // 100) % 10
    tens = (f // 10) % 10
    units = f % 10

    sum_even = ten_thousands + hundreds + units
    sum_odd = hundred_thousands + thousand + tens

    if sum_even == sum_odd:
        print(f, end=' ')