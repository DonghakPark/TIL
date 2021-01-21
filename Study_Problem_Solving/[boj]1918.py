"""
후위 표기식 문제
author : donghak park
contac: donghark03@naver.com
TODO : 다시 풀어볼것
"""

S = list(input())

answer = ""

op = []
alpha = []

while S:
    temp = S.pop(0)

    #알파벳일 경우
    if temp.isalpha():
        answer += temp

    else:
        if temp == "(":
            op.append(temp)

        elif temp == "*" or temp == "/":
            while op and (op[-1] == "*" or op[-1] == "/"):
                answer += op.pop()
            op.append(temp)

        elif temp == "+" or temp == "-":
            while op and op[-1] != "(":
                answer += op.pop()
            op.append(temp)

        elif temp == ")":
            while op and op[-1] != "(":
                answer += op.pop()
            op.pop()

while op:
    answer += op.pop()

print(answer)
