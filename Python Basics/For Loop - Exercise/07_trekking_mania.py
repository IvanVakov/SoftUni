count_groups = int(input())

musala_sum = 0
monblan_sum = 0
kilimandjaro_sum = 0
k2_sum = 0
everest_sum = 0
total_sum = 0
for i in range(1, count_groups + 1):
    count_people = int(input())
    total_sum = total_sum + count_people

    if count_people <= 5:
        musala_sum = musala_sum + count_people
    elif count_people <= 12:
        monblan_sum = monblan_sum + count_people
    elif count_people <= 25:
        kilimandjaro_sum = kilimandjaro_sum + count_people
    elif count_people <= 40:
        k2_sum = k2_sum + count_people
    elif count_people >= 41:
        everest_sum = everest_sum + count_people

percent_musala = musala_sum / total_sum * 100
print(f'{percent_musala:.2f}%')
percent_monblan = monblan_sum / total_sum * 100
print(f'{percent_monblan:.2f}%')
percent_kilimandjaro = kilimandjaro_sum / total_sum * 100
print(f'{percent_kilimandjaro:.2f}%')
percent_k2 = k2_sum / total_sum * 100
print(f'{percent_k2:.2f}%')
percent_everest = everest_sum / total_sum * 100
print(f'{percent_everest:.2f}%')
