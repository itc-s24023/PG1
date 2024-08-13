from datetime import date

day_now = date.today()
print(day_now)

xday = date(2006, 1, 26)
td = day_now - xday
print(td)
