# Enter your code here
is_weekday = True
is_holiday = True
no_school_today = is_weekday or is_holiday
print("There is no school today: " + str(no_school_today))

no_school_today = is_weekday and not(is_holiday)
print("There is no school today: " + str(no_school_today))