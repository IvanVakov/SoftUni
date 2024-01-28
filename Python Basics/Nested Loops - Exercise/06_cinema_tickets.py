studentscounter = 0
kidscounter = 0
standardcounter = 0
totalticketscounter = 0
command = input()
while command != "Finish":
    total_spaces = int(input())
    movie_name = command
    sold_movie_tickets = 0
    free_spaces = total_spaces
    while free_spaces > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        if ticket_type == "student":
            studentscounter += 1
        elif ticket_type == "standard":
            standardcounter += 1
        else:
            kidscounter += 1
        totalticketscounter += 1
        sold_movie_tickets += 1
        free_spaces-=1
    print(f"{command} - {sold_movie_tickets / total_spaces * 100:.2f}% full.")
    command = input()
print(f"Total tickets: {totalticketscounter}")
print(f"{(studentscounter/ totalticketscounter * 100):.2f}% student tickets.")
print(f"{standardcounter/ totalticketscounter * 100:.2f}% standard tickets.")
print(f"{kidscounter/ totalticketscounter * 100:.2f}% kids tickets.")