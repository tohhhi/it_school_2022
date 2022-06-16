from datetime import date, datetime

b_day = datetime(1998, 9 , 8)

delta = datetime.now() - b_day

print(delta)



this_year = datetime(2022, 1, 1)

delta = datetime.now() - this_year

print(delta)


print(delta.total_seconds()/3600)