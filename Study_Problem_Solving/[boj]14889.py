"""
스타트와 링크 문제
author : donghak park
contact: donghark03@naver.com
"""

def cal_diff(team1, team2):
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)

def make_team(team1, count, N, start):
    global answer

    if count == N//2:
        team2 = []
        for i in range(N):
            if i not in team1:
                team2.append(i)

        local_diff = cal_diff(team1, team2)
        answer = min(answer, local_diff)
        return

    for i in range(start, N):
        if i not in team1:
            team1.append(i)
            make_team(team1, count+1, N, i+1)
            team1.remove(i)

if __name__=="__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = int(1e9)
    make_team([], 0, N, 0)

    print(answer)