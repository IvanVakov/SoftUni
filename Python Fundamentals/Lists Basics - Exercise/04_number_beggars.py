single_string = input().split(", ")
beggars = int(input())

list_of_beggars = []
count = 0

for begar in range(beggars):
    each_beggar = 0

    for index in range(count, len(single_string), beggars):
        each_beggar += int(single_string[index])

    list_of_beggars.append(each_beggar)

    count += 1

print(list_of_beggars)