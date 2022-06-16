from datetime import datetime

#  3. Print current date formatted as dd/mmm/yy

yy = datetime.now().strftime("%d/%m/%Y")

print(yy)