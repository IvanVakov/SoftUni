exam_hour = int(input())
minutes_exam = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_all_min = (exam_hour * 60) + minutes_exam
arrival_all_min = (arrival_hours * 60) + arrival_minutes

diff_min = abs(exam_all_min - arrival_all_min)

if arrival_all_min > exam_all_min:
    print('Late')
    if diff_min >= 60:
        hours = diff_min // 60
        minutes = diff_min % 60
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif exam_all_min == arrival_all_min or diff_min <= 30:
    print('On time')
    if diff_min > 0:
        print(f"{diff_min} minutes before the start")
else:
    print('Early')
    if diff_min >= 60:
        hours = diff_min // 60
        minutes = diff_min % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{diff_min} minutes before the start")