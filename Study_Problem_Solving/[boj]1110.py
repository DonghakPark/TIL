"""
더하기 사이클 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

N = int(input())

time = 0
temp = str(N)
while True:
    if time != 0 and int(temp) == N:
        break

    temp2 = ''

    if int(temp) < 10:
        temp2 = "0" + temp
    else:
        temp2 = str(int(temp[0]) + int(temp[1]))

    temp = temp[-1] + temp2[-1]
    time += 1
print(time)