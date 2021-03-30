"""
2021 상반기 코딩테스트 대비 연습 문제 풀이
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import defaultdict


def solution(n, recipes, orders):

    fire = [[0,0,0] for _ in range(n)]

    reci = defaultdict(int)
    for element in recipes:
        menu, cook_time = element.split()
        reci[menu] = int(cook_time)

    order_converted = []
    for element in orders:
        menu, order_time = element.split()
        order_converted.append([menu, int(order_time), False])
    order_converted[-1][-1] = True

    time = 1
    while True:
        # 완료된 음식이 있으면서 마지막 음식일 경우 함수 종료
        for i in range(n):
            if fire[i][1] == 0:

                if fire[i][2] is True:
                    return time

        # 주문이 들어오면 Q에 넣기
        if order_converted and order_converted[0][1] <= time:
            empty_fire = -1
            for i in range(n):
                if fire[i][1] == 0:
                    empty_fire = i
                    break
            if empty_fire != -1:
                menu, _, final = order_converted.pop(0)
                fire[empty_fire] = [menu, reci[menu], final]

        # 요리
        for i in range(n):
            if fire[i][1] > 0:
                fire[i][1] -= 1

        time += 1

if __name__=="__main__":
    n = [2,3,1]
    recipes = [
        ["A 3", "B 2"],
        ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"],
        ["COOKIE 10000"]
    ]
    orders = [
        ["A 1", "A 2", "B 3", "B 4"],
        ["PIZZA 1","FRIEDRICE 2","SPAGHETTI 4","SPAGHETTI 6","PIZZA 7","SPAGHETTI 8"],
        ["COOKIE 300000"]
    ]
    result = [7, 12, 310000]

    for i in range(3):
        if solution(n[i], recipes[i], orders[i]) == result[i]:
            print("{}번 Test_case 정답입니다.".format(i))
        else:
            print("{}번 Test_case 틀렸습니다.".format(i))



