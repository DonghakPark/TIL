"""
풀었음
"""
T = int(input())
for test_case in range(T):
    N = int(input())
    names = []
    for _ in range(N):
        temp = input()
        names.append(temp)
    names = list(set(names))
    names = sorted(names, key=lambda x: (len(x), x))

    print("#{}".format(test_case + 1))
    for element in names:
        print(element)
