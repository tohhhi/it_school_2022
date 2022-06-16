from datetime import datetime


# 2. Print only time, formatted HH:mm:ss


clock = datetime.now().strftime("%H:%M:%S")

print(clock)