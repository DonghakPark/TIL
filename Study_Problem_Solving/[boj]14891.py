"""
톱니바퀴 문제
Author : Donghak Park
"""


def move_gear(Nth, direct):
    global gear

    now_left = gear[Nth][6]
    now_right = gear[Nth][2]

    if direct == 1:
        temp = gear[Nth].pop()
        gear[Nth].insert(0, temp)
    else:
        temp = gear[Nth].pop(0)
        gear[Nth].append(temp)

    move_left(Nth - 1, direct * -1, now_left)
    move_right(Nth + 1, direct * -1, now_right)

def move_left(Nth, direct, now_left):
    global gear

    if Nth <= 0:
        return

    if now_left == gear[Nth][2]:
        return
    else:
        now_left = gear[Nth][6]

        if direct == 1:
            temp = gear[Nth].pop()
            gear[Nth].insert(0, temp)
        else:
            temp = gear[Nth].pop(0)
            gear[Nth].append(temp)

        move_left(Nth - 1, direct * -1, now_left)


def move_right(Nth, direct, now_right):
    global gear

    if Nth >= 5:
        return

    if now_right == gear[Nth][6]:
        return
    else:

        now_right = gear[Nth][2]
        if direct == 1:
            temp = gear[Nth].pop()
            gear[Nth].insert(0, temp)
        else:
            temp = gear[Nth].pop(0)
            gear[Nth].append(temp)

        move_right(Nth + 1, direct * -1, now_right)


# 2번이 오른쪽 6번이 왼쪽 N극이 0
gear = {}
answer = 0

for i in range(1, 5):
    gear[i] = list(map(int, list(input())))

K = int(input())

for _ in range(K):
    Nth, direct = map(int, input().split())
    move_gear(Nth, direct)

for key in gear.keys():
    if gear[key][0] == 1:
        answer += (2 ** (key - 1))

print(answer)
