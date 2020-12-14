N = int(input())
Arr = []
for i in range(N):
    x,y = map(int, input().split())
    Arr.append([x,y])

Arr.sort(key=lambda x : (x[1],x[0]))

for element in Arr:
    print(element[0],element[1])