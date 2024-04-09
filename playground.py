import datetime
from math import sqrt

t0 = datetime.datetime.now()

for e in range(10000000):
    sqrt(e)

t1 = datetime.datetime.now()
time = t1-t0
time.seconds + time.microseconds

print((t1-t0).microseconds)