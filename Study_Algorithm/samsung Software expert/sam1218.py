for test_case in range(1,10):
    Len = int(input())
    Str = input()
    a1, a2, a3, a4, a5,a6 ,a7 ,a8 = 0
    ans = 0
    for elements in range(1, Len+1):
        if Str[elements] == "[":
            a1 = a1 + 1
        elif Str[elements] == "]":
            a2 = a2 +1
        elif Str[elements] == "{":
            a3 = a3 +1
        elif Str[elements] == "}":
            a4 = a4 +1
        elif Str[elements] == "<":
            a5 = a5 +1
        elif Str[elements] == ">":
            a6 = a6 +1
        elif Str[elements] == "(":
            a7 = a7 +1
        elif Str[elements] == ")":
            a8 = a8 +1

    if a1 == a2 and a3 == a4 and a5 == a6 and a7 == a8:
        ans = 1
    else:
        ans = 0
    print("#%d %d" %(test_case, ans))
#  정답 stack 활용 예제뭄
# def func(chr):
#     global length
#     open = ['(','[','{','<']
#     close = [')',']','}','>']
#     result = 1
#     for i in range(length):
#         if chr[i] in open:
#             stack.append(chr[i])
#         if chr[i] in close:
#             if open.index(stack.pop()) == close.index(chr[i]):
#                 continue
#             else:
#                 result = 0
#                 break
#     if stack:
#         result = 0
#     return result
#  
# for tc in range(1, 11):
#     length = int(input())
#     text = list(input())
#     stack = []
#     print('#{} {}'.format(tc, func(text)))
