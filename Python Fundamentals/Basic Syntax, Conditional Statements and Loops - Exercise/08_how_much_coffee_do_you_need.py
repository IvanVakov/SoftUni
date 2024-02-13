command = input()
coffee_counter = 0
events = ['dog', 'cat', 'coding', 'movie', ]

while command != 'END':

    if command.lower() in events:
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print(f"You need extra sleep")
else:
    print(coffee_counter)