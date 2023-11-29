month = input()
count_nights = int(input())
apartment_price = 0
studio_price = 0

if month == 'May' or month == 'October':
    apartment_price = count_nights * 65
    studio_price = count_nights * 50
elif month == 'June' or month == 'September':
    apartment_price = count_nights * 68.70
    studio_price = count_nights * 75.20
elif month == 'July' or month == 'August':
    apartment_price = count_nights * 77
    studio_price = count_nights * 76

if count_nights > 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.7
elif count_nights > 7 and (month == 'May' or month == 'October'):
    studio_price = studio_price * 0.95
elif count_nights > 14 and (month == 'June' or month == 'September'):
    studio_price = studio_price * 0.8

if count_nights > 14:
    apartment_price = apartment_price * 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")