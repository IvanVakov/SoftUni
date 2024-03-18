num = int(input())

list_positive = []
list_negative = []

for _ in range(num):
    numbers = int(input())

    if numbers >= 0:
        list_positive.append(numbers)
    else:
        list_negative.append(numbers)

print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}")
print(f"Sum of negatives: {sum(list_negative)}")