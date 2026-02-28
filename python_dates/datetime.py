import datetime
somedate = datetime.date(2020,11,11)
print(somedate.day)
print(somedate.year)
print(datetime.date.today())

sometime = datetime.time(20,30,40,10)


first_date = datetime.date(2018, 3, 1)
second_date = datetime.date(2023, 10, 2)

new = second_date - first_date
print(new.strftime("%Y-%m-%d"))
tz = datetime.timezone(datetime.timedelta(hours=3))
