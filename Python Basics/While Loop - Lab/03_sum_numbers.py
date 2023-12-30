number = int(input())
total_sum = 0


while True:
    data = int(input())
    total_sum += data

    if total_sum >= number:
        print(total_sum)
        break
