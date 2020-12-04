N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))
arr.sort()

for element in arr:
    print(element)