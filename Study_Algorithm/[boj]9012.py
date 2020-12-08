tc = int(input())

for test_case in range(tc):
    S = input()
    stack = []

    for element in S:
        stack.append(element)

        if len(stack) >= 2:
            if stack[-2] == "(" and stack[-1] == ")":
                stack.pop()
                stack.pop()
        else:
            continue
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")