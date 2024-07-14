line = input()
company_users = {}

while line != 'End':
    command = line.split(" -> ")
    company_name = command[0]
    employees_id = command[1]

    if company_name not in company_users:
        company_users[company_name] = []

    if employees_id not in company_users[company_name]:
        company_users[company_name].append(employees_id)

    line = input()

for company, employees in company_users.items():
    print(company)
    for employee in employees:
        print(f"-- {employee}")
