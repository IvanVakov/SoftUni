import re

text = input().lower()
sub_text = input().lower()

pattern = rf"\b{sub_text}\b"

matches = re.findall(pattern, text)

print(len(matches))