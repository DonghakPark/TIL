def solution(str):
    temp_arr = list(str)
    S = []
    for i in range(0, len(temp_arr)):
        S.append(temp_arr.pop(0))
        if len(S) <= 1:
            continue
        else:
            if(S[-1]==')' and S[-2] == '(' ):
                S.pop()
                S.pop()
    answer = len(S)
    return answer

if __name__=="__main__":
    str = '(()))'
    str2 = '(())(())())(((()))))()())(((()))'
    str3 = ')))))((((('
    print("Case1")
    print(solution(str))

    print("Case2")
    print(solution(str2))
    print("Case3")
    print(solution(str3))
