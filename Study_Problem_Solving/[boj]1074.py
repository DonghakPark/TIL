import math

N, r, c = map(int, input().split())

answer = 0
y = int(math.pow(2,N)/2)
x = int(math.pow(2,N)/2)

while N>0:
    N -= 1

    temp = int(math.pow(2,N)/2)
    skip = int(math.pow(4,N))

    #1사분면
    if r < y and c < x :
        x -= temp
        y -= temp

    #2사분면
    elif r < y and c >= x :
        x += temp
        y -= temp
        answer += skip

    #3사분면
    elif r >= y and c < x :
        x -= temp
        y += temp
        answer += skip * 2

    #4사분면
    elif r >= y and c >= x :
        x += temp
        y += temp
        answer += skip * 3

print(answer)