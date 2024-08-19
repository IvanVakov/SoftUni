import re

text = input()

pattern = r"\b(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z][a-z])\2(?P<Year>\d{4})\b"

dates = re.finditer(pattern, text)

for date in dates:
    data = date.groupdict()
    print(f"Day: {date['Day']}, Month: {data['Month']}, Year: {data['Year']}")