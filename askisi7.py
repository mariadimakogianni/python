import datetime
now = datetime.datetime.now()
year=now.year
month= now.month
day= now.day
daywe=datetime.datetime.today().weekday()
p=0
for x in range (year+1, year+11):
    for j in range (1,12):
        future=datetime.datetime(x, month, day)
        if daywe==future.weekday():
            p=p+1
print p



