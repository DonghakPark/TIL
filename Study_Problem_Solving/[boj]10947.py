import random
arr = []

while len(arr) < 6:
    temp = random.randrange(1,46)

    if temp in arr:
        continue
    else:
        arr.append(temp)
arr.sort()

print(arr)