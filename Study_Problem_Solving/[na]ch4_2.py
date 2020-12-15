N = int(input())
count = 0
h = 0
m = 0
s = 0

while h <= N:
    s += 1

    if s >= 60:
        m += 1
        s = 0

    if m >= 60:
        h += 1
        m = 0

    if '3' in str(h)+str(m)+str(s):
        count += 1

print(count)