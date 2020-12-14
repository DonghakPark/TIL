arr = []
for i in range(10):
    arr.append(int(input()))

answer = []

for i in range(10):
    answer.append(arr[i]%42)

answer = set(answer)
print(len(answer))