import sys
from collections import Counter

def avg(arr):
    return round(sum(arr)/len(arr))

def mid(arr):
    arr.sort()
    return arr[(len(arr)//2)]

def fre(arr):
    k = Counter(arr).most_common()
    if len(arr) > 1:
        if k[0][1] == k[1][1]:
            return k[1][0]
        else:
            return k[0][0]
    else:
        return k[0][0]

def ran(arr):
    return max(arr) - min(arr)

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

print(avg(arr))
print(mid(arr))
print(fre(arr))
print(ran(arr))