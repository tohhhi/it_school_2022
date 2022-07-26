from datetime import datetime

print(datetime.now().strftime("%d/%b/%y"))


b_day = datetime(1998,9,8)

print(b_day.strftime("%m/%d/%Y"))


current_year = datetime(2022,1,1)

delta = datetime.now() - current_year

print(delta)



# cate zile au mai ramas din acest an

final_year = datetime(2023,1,1)

delta_2 = final_year - datetime.now()

print(delta_2)