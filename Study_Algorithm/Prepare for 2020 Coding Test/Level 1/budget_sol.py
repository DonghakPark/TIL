"""
작성자 : Donghak Park
작성일 : 2020.09.05
풀이 : Sorting을 통해서 순서대로 budget에 넣고 이가 예산을 충족하는지 검사
"""
def solution(d, budget):
    answer = 0
    d.sort()
    temp_budget = 0
    for element in d:
        if temp_budget + element <= budget:
            temp_budget += element
            answer += 1
        else:
            break

    return answer

if __name__=="__main__":
    d1 = [1,3,2,5,4]
    d2 = [2,2,3,3]

    print(solution(d1,budget=9)) #answer = 3
    print(solution(d2,budget=10)) #answer =4