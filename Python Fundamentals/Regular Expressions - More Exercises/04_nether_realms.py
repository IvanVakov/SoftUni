import re

demons = ''.join(input().split()).split(",")
demon_book = {}

demon_health_pattern = re.compile(r'(?P<name>[^\d\+\-*\/\.])')
demon_damage_pattern = re.compile(r'(?:\\+|-)?[0-9]+(?:\.[0-9]+)?')
demon_operators_pattern = re.compile(r'([*\/])')


for current_demon in demons:
    health_of_demon = demon_health_pattern.finditer(current_demon)
    demon_health = sum([ord(letter['name']) for letter in health_of_demon])

    damage_of_demon = demon_damage_pattern.finditer(current_demon)
    demon_damage = sum([float(digit[0]) for digit in damage_of_demon])

    demon_book[current_demon] = demon_book.get(current_demon, {'health': demon_health, 'damage': demon_damage})
    find_operators = demon_operators_pattern.finditer(current_demon)
    for operator in find_operators:
        if operator[0] == "*":
            demon_book[current_demon]['damage'] *= 2
        elif operator[0] == "/":
            demon_book[current_demon]['damage'] /= 2
for demon in sorted(demon_book):
    print(f"{demon} - {demon_book[demon]['health']} health, {demon_book[demon]['damage']:.2f} damage")
