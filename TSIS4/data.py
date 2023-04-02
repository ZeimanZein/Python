import datetime
day = datetime.date.today()-datetime.timedelta(5)
print(f"5 days before {day}")
yesterday = datetime.date.today()-datetime.timedelta(1)
today = datetime.date.today()
tomorrow = datetime.date.today()+datetime.timedelta(1)
print(f"Yesterday:{yesterday}, Today:{today}, Tomorrow:{tomorrow}")
micro = datetime.datetime.today().replace(microsecond=0)

print("Enter a number:", micro)

dt1 = datetime.datetime(2022, 3, 9, 12, 30, 45)
dt2 = datetime.datetime(2022, 3, 10, 14, 45, 30)

diff_seconds = (dt2 - dt1).total_seconds()

print('The difference between the two dates is', diff_seconds, 'seconds')