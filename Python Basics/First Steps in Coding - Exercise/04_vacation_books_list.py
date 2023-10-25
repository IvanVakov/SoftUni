count_page = int(input())
pages_per_hour = int(input())
count_days = int(input())

needed_hours = count_page / pages_per_hour // count_days

print(needed_hours)