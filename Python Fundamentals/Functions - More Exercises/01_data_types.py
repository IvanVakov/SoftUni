type_data = input()
data = input()


def types(command, s):
    if command == 'int':
        index = int(s)
        result = index * 2
        print(result)
    elif command == 'real':
        index = float(s)
        result = index * 1.5
        print(f'{result:.2f}')
    elif command == 'string':
        print(f'${s}$')


types(type_data, data)