def solution(winnum, bonus, usernum):
    winnum = set(winnum)
    usernum = set(usernum)

    bonus_check = False

    if bonus in usernum:
        bonus_check = True
    # 보너스 숫자가 포함되는지 체크

    matches = len(winnum & usernum)

    if matches == 6:
        return 1
    elif matches == 5 and bonus_check == True:
        return 2
    elif matches == 5:
        return 3
    elif matches == 4:
        return 4
    elif matches == 3:
        return 5
    else:
        return -1


if __name__=="__main__":
    winnum = [1,11,12,14,26,35]
    bonus = 6
    usernum = [1,35,11,14,12,26]
    print(solution(winnum, bonus, usernum))