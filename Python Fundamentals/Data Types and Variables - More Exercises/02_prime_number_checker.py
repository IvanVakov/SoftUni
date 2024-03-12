prime_number = int(input())
flag = False
if prime_number > 1:
    for i in range(2, prime_number):
        if prime_number % i == 0:
            flag = True
            break
if flag:
    print('False')
else:
    print('True')