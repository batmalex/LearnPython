# import locale
# locale.setlocale(locale.LC_TIME, "ru_RU")
from datetime import datetime, timedelta


dt_now = datetime.now()
dt2 = datetime(2015, 5, 16, 8, 3, 44)
print(dt_now, dt2)
delta = dt_now - dt2
print(delta)
dt3 = dt2 + delta
print(dt3)
delta = timedelta(days=10)
print(delta)

print(dt_now.strftime('%d/%m/%Y %H:%m'))
print(dt_now.strftime('%A %d %B %Y'))
string_from_file = '12/23/2010'
date_new = datetime.strptime(string_from_file, '%m/%d/%Y')
print(date_new)
