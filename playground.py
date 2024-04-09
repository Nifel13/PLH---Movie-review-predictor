import datetime
from math import sqrt

t0 = datetime.datetime.now()

for e in range(100000000):
    sqrt(e)

t1 = datetime.datetime.now()
time = t1-t0
x = time.seconds + float(f'0.{time.microseconds}')

print(x)