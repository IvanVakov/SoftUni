import re

links = []
while True:
    line = input()
    if not line:
        break
    pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"

    matches = re.findall(pattern, line)
    links.extend([m[0] for m in matches])

for link in links:
    print(link)
