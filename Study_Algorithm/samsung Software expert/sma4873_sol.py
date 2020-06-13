T = int(input())
for t in range(1,T+1):
    Str = input()
    Str_Arr = list(Str)
    Stack = []
    for s in Str_Arr:
        Stack.append(s)
        if len(Stack) <= 1:
            continue
        else:
            if(Stack[-1] == Stack[-2]):
                Stack.pop()
                Stack.pop()

    print("#{} {}".format(t, len(Stack)))

