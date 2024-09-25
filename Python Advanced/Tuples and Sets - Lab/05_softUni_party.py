number_of_guest = int(input())
reservation = set()

for _ in range(number_of_guest):
    reservation_code = input()
    reservation.add(reservation_code)

guests = input()

while guests != "END":
    reservation.remove(guests)
    guests = input()

print(len(reservation))
print("\n".join(sorted(reservation)))
