import time
from datetime import datetime

while True:
    time.sleep(1)
    if datetime.now().second == 30:
        print("Jumatate de minut!")



