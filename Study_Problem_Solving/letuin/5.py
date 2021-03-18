# FSM (유한 상태 머신 ) 으로 풀이 가능
# 연습해 보기

def cal_score(now, bonus, total):
    for i in range(11):
        total[i] += now[i][0] * bonus[i][0]
        total[i] += now[i][1] * bonus[i][1]
    return sum(total)


throw = list(map(int, input().split()))
answer = []

now = [[0, 0] for _ in range(11)]
bonus = [[1, 1] for _ in range(11)]
total = [0] * 11
frame = 0
count = 0
flag_strike = False
flag_spare = False

while throw:
    element = throw.pop(0)

    if frame == 10:
        if flag_spare is True:
            now[frame][0] = throw.pop(0)
        elif flag_strike is True:
            now[frame][0] = throw.pop(0)
            now[frame][1] = throw.pop(0)

        answer.append(cal_score(now, bonus, total))
        print(now)
        print(bonus)
        print(total)

        now = [[0, 0] for _ in range(11)]
        bonus = [[1, 1] for _ in range(11)]
        total = [0] * 10

        frame = 0
        count = 0
        flag_strike = False
        flag_spare = False

    # 스트라이크 일 경우
    if element == 10:
        if frame == 9:
            flag_strike = True
        bonus[frame + 1] = [2, 2]
        now[frame] = [10, 0]
        frame += 1
    # 다른 경우
    else:
        now[frame][count] = element

        count += 1

        if sum(now[frame]) == 10:
            bonus[frame + 1] = [2, 1]
            flag_spare = True

        if count == 2:
            count = 0
            frame += 1

print(answer)
