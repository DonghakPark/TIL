T = int(input())

for t in range(1,T+1):
    Str = input()
    target = ['(', ')', "{", "}"]
    stack = []
    for i in Str:
        if i in target:
            stack.append(i)
        if len(stack) <=1:
            continue
        else:
            if stack[-1] == ')' and stack[-2] =='(':
                stack.pop()
                stack.pop()
            elif stack[-1] == '}' and stack[-2] == '{':
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t,0))