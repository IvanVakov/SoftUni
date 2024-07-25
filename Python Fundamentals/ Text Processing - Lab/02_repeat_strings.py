text = input().split()
repeat_text = ""

for word in text:
    repeat_text += word * len(word)


print(repeat_text)