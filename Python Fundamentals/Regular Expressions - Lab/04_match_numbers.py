import re

text = input()

patten = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

matches = re.finditer(patten, text)

for match in matches:
    print(match.group(), end=" ")