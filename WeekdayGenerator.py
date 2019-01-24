from datetime import date
from datetime import timedelta
import calendar
from datetime import datetime

my_date = date.today()
day_today = calendar.day_name[my_date.weekday()]
print(day_today)

# timedelta(days=1)

# print datetime.now() + timedelta(days=1)

day_plus1 = datetime.now() + timedelta(days=1)
d1 = calendar.day_name[day_plus1.weekday()]
print(d1)


day_plus2 = datetime.now() + timedelta(days=2)
d2 = calendar.day_name[day_plus2.weekday()]
print(d2)


day_plus3 = datetime.now() + timedelta(days=3)
d3 = calendar.day_name[day_plus3.weekday()]
print(d3)


day_plus4 = datetime.now() + timedelta(days=4)
d4 = calendar.day_name[day_plus4.weekday()]
print(d4)

day_plus5 = datetime.now() + timedelta(days=5)
d5 = calendar.day_name[day_plus5.weekday()]
print(d5)

day_plus6 = datetime.now() + timedelta(days=6)
d6 = calendar.day_name[day_plus6.weekday()]
print(d6)