N = int(input())
arr = []
for i in range(N):
    x, y = input().split()
    arr.append([int(x), y, i])

arr.sort(key = lambda x:(x[0], x[2]))

for element in arr:
    print("{} {}".format(element[0], element[1]))