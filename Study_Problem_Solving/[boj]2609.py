A,B = map(int, input().split())

for i in range(min(A,B), 0, -1):
    if A%i ==0 and B%i ==0:
        print(i)
        break
start = max(A,B)
while True:
    if start%A == 0 and start%B == 0:
        print(start)
        break
    else:
        start += 1
