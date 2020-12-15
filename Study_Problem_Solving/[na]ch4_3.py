"""
왕실의 나이트 문제
"""

a = input()
x = int(a[1])
y = ord(a[0]) - 96

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        count += 1

print(count)