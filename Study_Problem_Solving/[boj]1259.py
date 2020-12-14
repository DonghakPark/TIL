import copy

while(True):
    a = input()
    if a == '0':
        break
    else:
        a = list(a)
        b = copy.deepcopy(a)
        a.reverse()
        if a == b:
            print("yes")
        else:
            print("no")