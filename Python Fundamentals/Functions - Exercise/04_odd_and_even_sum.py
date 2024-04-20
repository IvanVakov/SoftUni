def odd_and_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for current_num in num:
        if int(current_num) % 2 != 0:
            odd_sum += int(current_num)
        else:
            even_sum += int(current_num)
    return odd_sum, even_sum


number = input()
odd_sum, even_sum = odd_and_even_sum(number)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")