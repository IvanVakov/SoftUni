sum_deposit = float(input())
time_deposit_months = int(input())
annual_interest_rate = float(input())

rate = sum_deposit * annual_interest_rate /100
rate_for_month = rate / 12
total_sum = sum_deposit + time_deposit_months * rate_for_month


print(total_sum)