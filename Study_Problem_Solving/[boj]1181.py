N = int(input())
arr = []
arr2 = []
for i in range(N):
    s = input()
    if s not in arr2:
        arr2.append(s)
        arr.append([len(s), s])

arr.sort()
for i in arr:
    print(i[1])