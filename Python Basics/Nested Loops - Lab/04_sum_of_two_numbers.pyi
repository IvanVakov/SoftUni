start_number = int(input())
end_number = int(input())
magic_number = int(input())

combination = 0
is_found = False

for n in range(start_number, end_number + 1):
    for m in range(start_number, end_number + 1):
        combination += 1

        if n + m == magic_number:
            print(f'Combination N:{combination} ({n} + {m} = {magic_number})')
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{combination} combinations - neither equals {magic_number}")