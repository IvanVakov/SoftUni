text = input()
parenthesis = []

for index in range(len(text)):
  if text[index] == "(":
    parenthesis.append(index)

  elif text[index] == ")":
    first_element = parenthesis.pop()
    last_element = index + 1
    print(text[first_element:last_element])