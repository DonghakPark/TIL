def solution(lottos, win_nums):
    answer = []
    zero_num = lottos.count(0)

    while True:
        if 0 in lottos:
            lottos.remove(0)
        else:
            break

    lottos.sort()

    hit_num = 0
    while lottos:
        now = lottos.pop(0)
        if now in win_nums:
            hit_num += 1

    max_hit, min_hit = 7 - (zero_num + hit_num), 7 - hit_num

    if max_hit > 5:
        answer.append(6)
    else:
        answer.append(max_hit)

    if min_hit > 5:
        answer.append(6)
    else:
        answer.append(min_hit)

    return answer