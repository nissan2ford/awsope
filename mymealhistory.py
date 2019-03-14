import datetime

today = datetime.datetime.now()

todaystr = '{0:%Y%m%d}'.format(today)

print('todaystr = '+todaystr)

todaywday = today.strftime('%a')

print('todaywday = '+todaywday)
