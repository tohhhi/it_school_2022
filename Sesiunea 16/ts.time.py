import time
# de la timestamp la data/ora formatata

some_ts = 1655225147.8209023

ts_struct = time.gmtime(some_ts)

print(ts_struct.tm_hour)
print(ts_struct.tm_min)


print(time.strftime("%m/%d/%Y", ts_struct))