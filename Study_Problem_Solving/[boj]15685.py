"""
드래곤 커브 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def make_dragon_curve(x,y,d,g,count):
    global arr_map
    if count == g+1:
        return

    arr_map[y][x] = 1
    a, b = x, y
    for i in range(count+1):
        nx = a + dx[(d + i) % 4]
        ny = b + dy[(d + i) % 4]
        arr_map[ny][nx] = 1
        a, b = nx, ny

    count += 1
    make_dragon_curve(a,b,(d+count)%4, g, count)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

arr_map = [[0] * 10 for _ in range(10)]

for x,y,d,g in arr:
    make_dragon_curve(x,y,d,g,0)

print(arr)
print(arr_map)