while True:
    S = input()

    if S == ".":
        break
    else:
        stack = []
        target = ["(",")","[","]"]
        for element in S:
            if element in target:
                if len(stack) != 0:
                    if stack[-1] =="(" and element ==")":
                        stack.pop()
                    elif stack[-1] == "[" and element =="]":
                        stack.pop()
                    else:
                        stack.append(element)
                else:
                    stack.append(element)
            else:
                continue

        if len(stack) == 0:
            print("yes")
        else:
            print("no")

