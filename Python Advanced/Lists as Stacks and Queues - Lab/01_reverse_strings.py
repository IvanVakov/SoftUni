text = list(input())
list_as_stack = []

for i in range(len(text)):
    list_as_stack.append(text.pop())

print("".join(list_as_stack))