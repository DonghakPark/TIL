"""
2021 상반기 코딩테스트 대비 연습 문제 풀이
Author : DongHak Park
Contact: donghark03@naver.com
"""
import datetime


def solution(holidaty, k):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    converted_date = []

    for element in holidaty:
        mon, day = element.split("/")
        converted_date.append(sum(month[:int(mon)-1]) + int(day))

    sat = 2
    sun = 3

    while sat <= 365 and sun <= 365:
        if sat not in converted_date:
            converted_date.append(sat)
        if sun not in converted_date:
            converted_date.append(sun)
        sat += 7
        sun += 7
    converted_date.sort()

    answer = []
    count = 1
    for i in range(len(converted_date) - 1):
        if converted_date[i+1] - 1 == converted_date[i]:
            count += 1
        else:
            if count not in answer:
                answer.append(count)
            count = 1

    answer.sort(reverse=True)

    if k > len(answer):
        return 1
    else:
        return answer[k-1]


if __name__=="__main__":
    holidays = [["01/14", "01/15", "01/18", "01/22", "01/23", "01/29", "02/01", "02/03", "02/07"],
                ["01/14", "01/15", "01/18", "01/22", "01/23", "01/29", "02/01", "02/03", "02/07"],
                ["01/14", "01/15", "01/18", "01/22", "01/23", "01/29", "02/01", "02/03", "02/07"],
                ["01/14", "01/15", "01/18", "01/22", "01/23", "01/29", "02/01", "02/03", "02/07"],
                ["01/14", "01/15", "01/18", "01/22", "01/23", "01/29", "02/01", "02/03", "02/07"]
                ]
    k = [1,2,3,4,5]
    answer = [5,4,3,2,1]
    for i in range(5):
        if solution(holidays[i], k[i]) == answer[i]:
            print("{}번 Test_case 정답입니다.".format(i))
        else:
            print("{}번 Test_case 틀렸습니다.".format(i))
