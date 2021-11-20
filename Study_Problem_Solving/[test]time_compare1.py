"""
Author : Donghak Park
"""
from collections import defaultdict
import time
a = [False] * 10000000
b = {}
for i in range(0,10000000):
    b[i] = False
c = defaultdict(bool)

start = time.time()
for i in range(10000000):
    a[i] = True
print("list time : ", time.time() - start)

start = time.time()
for i in range(10000000):
    b[i] = True
print("dict time : ", time.time() - start)

start = time.time()
for i in range(10000000):
    c[i] = True
print("defaultdict time : ", time.time() - start)
