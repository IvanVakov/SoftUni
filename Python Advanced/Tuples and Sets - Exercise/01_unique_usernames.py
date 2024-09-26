number_of_usernames = int(input())
unique_username = set()

for _ in range(number_of_usernames):
    unique_username.add(input())

print(*unique_username, sep="\n")