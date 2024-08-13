from datetime import datetime
now = datetime.today()
print(now)  #現在年月日分秒マイクロ秒
print(now.year)   #現在年
print(now.month)   #現在月
print(now.day)   #現在日
print(now.hour)   #現在時
print(now.minute)   #現在分
print(now.second)   #現在病
print(now.microsecond)   #現在マイクロ秒

dt = datetime.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M")
print(dt)
dt2 = dt.strftime("%Y年%m月%d日 %H時%M分")
print(dt2)

import datetime
t_delta = datetime.timedelta(days=1)
dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt + t_delta)
