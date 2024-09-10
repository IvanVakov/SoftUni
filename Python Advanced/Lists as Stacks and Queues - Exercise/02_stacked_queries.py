from collections import deque

number = int(input())
stack_deque = deque()

for _ in range(number):
    data = [int(x) for x in input().split()]

    if data[0] == 1:
        stack_deque.append(data[1])

    elif data[0] == 2:
        if stack_deque:
            stack_deque.pop()

    elif data[0] == 3:
        if stack_deque:
            print(max(stack_deque))

    elif data[0] == 4:
        if stack_deque:
            print(min(stack_deque))

stack_deque.reverse()

print(*stack_deque, sep=", ")