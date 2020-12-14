import sys
N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([x,y])

answer = []

for element1 in arr:
    count = 0
    x1, y1 = element1
    for element2 in arr:
        x2, y2 = element2
        if x2 > x1 and y2 > y1:
            count += 1
    answer.append(count+1)

for element in answer:
    sys.stdout.write(str(element)+" ")
