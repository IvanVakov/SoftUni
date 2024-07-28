text = input()

digits = ""
letters = ""
symbols = ""

for word in text:
    if word.isdigit():
        digits += word
    elif word.isalnum():
        letters += word
    else:
        symbols += word

print(digits)
print(letters)
print(symbols)