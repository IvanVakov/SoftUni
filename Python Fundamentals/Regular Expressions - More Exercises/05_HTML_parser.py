import re

html_input = input()

title_match = re.search(r'<title>(.*?)<\/title>', html_input, re.DOTALL)
title = title_match.group(1) if title_match else ''

body_match = re.search(r'<body>(.*?)<\/body>', html_input, re.DOTALL)
body_content = body_match.group(1) if body_match else ''

clean_content = re.sub(r'<.*?>', '', body_content)

clean_content = re.sub(r'\s+', ' ', clean_content).strip()

print(f"Title: {title}")
print(f"Content: {clean_content}")
