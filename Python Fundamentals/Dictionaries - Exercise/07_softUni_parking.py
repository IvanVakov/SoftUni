count = int(input())
parking_lot = {}


for _ in range(count):
    line = input().split()
    command = line[0]
    username = line[1]

    if command == 'register':
        plate_number = line[2]

        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = plate_number
            print(f"{username} registered {plate_number} successfully")

    elif command == 'unregister':
        if username in parking_lot:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for name, number in parking_lot.items():
    print(f"{name} => {number}")