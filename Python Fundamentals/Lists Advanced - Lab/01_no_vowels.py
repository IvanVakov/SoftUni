text = input().lower()
my_list = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I',]
result = [ch for ch in text if ch not in my_list]
print(''.join(result))