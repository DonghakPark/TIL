def solution(s):
    answer =0
    Stack = []
    for i in s:
        Stack.append(i)
        if len(Stack) <= 1:
            continue
        else:
            if Stack[-1] == Stack[-2]:
                Stack.pop()
                Stack.pop()
    if len(Stack) == 0:
        answer =1

    return answer

if __name__=="__main__":
    s = "baabaa"
    print(solution(s))