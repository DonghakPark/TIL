"""
알파벳 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def solution(count, a, b):
    global answer
    global visited_alpha

    answer = max(answer, count)
    x, y = a, b
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited_alpha[alpha_map[nx][ny]] is False:
            visited_alpha[alpha_map[nx][ny]] = True
            solution(count+1, nx, ny)
            visited_alpha[alpha_map[nx][ny]] = False

R, C = map(int, input().split())
alpha_map = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(R)]

answer = 1
visited_alpha = [False] * 26
visited_alpha[alpha_map[0][0]] = True
solution(1,0,0)

print(answer)