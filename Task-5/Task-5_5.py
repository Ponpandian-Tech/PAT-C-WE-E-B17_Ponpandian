from datetime import datetime

date = datetime.now()

get_date = lambda d: (d.year, d.month, d.day)

print(get_date(date))