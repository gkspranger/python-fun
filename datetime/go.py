import datetime

mytime = datetime.time(hour=12, minute=30, second=59)

print(mytime)

print(mytime.second)

today = datetime.date.today()
mydate = datetime.date(year=2018, month=1, day=10)

print(today)
print(today.timetuple())
print(mydate)
print(today - mydate)
