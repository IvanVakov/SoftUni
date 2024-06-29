list_of_chars = input().split(", ")
print({char: ord(char) for char in list_of_chars})