"""
괄호 변환 문제
author : donghak park
contact : donghark03@naver.com
"""
#
# def reverse_s(w):
#     str = ""
#     for i in range(len(w)):
#         if w[i] == "(":
#             str +=  ")"
#         else:
#             str += "("
#     return str
#
# def check(w):
#     stack = []
#
#     for element in w:
#         stack.append(element)
#
#         if len(stack) > 1:
#             if stack[-2] == "(" and stack[-1] == ")":
#                 stack.pop()
#                 stack.pop()
#     if len(stack) == 0:
#         return True
#     else:
#         return False
# def make_uv(w):
#     count1=0
#     count2=0
#     for i in range(len(w)):
#         if w[i] == "(":
#             count1+=1
#         else:
#             count2+=1
#
#         if count1==count2:
#             return w[:i+1], w[i+1:]
#
# def process(w):
#     # 빈 문자열이면 반환
#     if w =="":
#         return ""
#
#     u,v = make_uv(w)
#
#     if check(u) == True:
#         if v != "":
#             v = process(v)
#         else:
#             print(u+v)
#             return u+v
#
#     else:
#         result = process(v)
#         temp = "(" + result + ")"
#         u = u[1:-1]
#         u = reverse_s(u)
#         print(temp + u)
#         return temp + u
#
#
# def solution(p):
#     answer = ''
#     if check(p) == True:
#         return p
#     else:
#         answer = process(p)
#         print(answer)
#         return answer

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)

    u = p[:index+1]
    v = p[index+1:]

    if check_proper(u):
        answer = u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

if __name__ == "__main__":
    p1 = "(()())()"
    p2 = ")("
    p3 = "()))((()"
    print(solution(p1))
    print(solution(p2))
    print(solution(p3))