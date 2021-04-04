from collections import defaultdict, deque


def solution(enroll, referral, seller, amount):
    answer = []

    # 딕셔너리 구성하기
    tree_parent = defaultdict(list)
    profit = defaultdict(int)

    for i in range(len(enroll)):
        start = referral[i]
        end = enroll[i]
        if start == "-":
            start = "center"

        tree_parent[end].append(start)
        profit[end] = 0

    for i in range(len(seller)):
        seller_name = seller[i]
        sell_amount = amount[i]
        Q = deque()
        Q.append([seller_name, sell_amount * 100])

        while Q:
            now_name, now_profit = Q.popleft()
            go_up = now_profit // 10
            mine = now_profit - go_up

            if tree_parent[now_name]:
                profit[now_name] += mine
                Q.append([tree_parent[now_name][0], go_up])
            else:
                profit[now_name] += now_profit
    for enroll_name in enroll:
        answer.append(profit[enroll_name])

    return answer