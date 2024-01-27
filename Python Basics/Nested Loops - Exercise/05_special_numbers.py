n = int(input())

for thousand in range(1, 10):
    for hundred in range(1, 10):
        for ten in range(1, 10):
            for init in range(1, 10):
                if n % thousand == 0 and n % hundred == 0 and n % ten == 0 and n % init == 0:
                    print(f'{thousand}{hundred}{ten}{init}', end=' ')

