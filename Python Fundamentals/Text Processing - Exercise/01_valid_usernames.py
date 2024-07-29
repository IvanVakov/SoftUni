from string import ascii_letters, digits

usernames = input().split(", ")
allowed_chars = ascii_letters + digits + "_" + "-"

for username in usernames:
    if len(username) < 3 or len(usernames) > 16:
        continue
    contains_forbidden_char = False
    for char in username:
        if char not in allowed_chars:
            contains_forbidden_char = True
            break

    if contains_forbidden_char:
        continue

    print(username)