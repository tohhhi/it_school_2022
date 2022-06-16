from datetime import datetime

# formatare data ora
print(datetime.now().strftime("%H:%M:%S"))


print(datetime.now().strftime("%d/%b/%y"))   # 14/Jun/22

# 09/08/1998

b_day = datetime(1998, 9 , 8)

print(b_day.strftime("%m.%d.%Y"))