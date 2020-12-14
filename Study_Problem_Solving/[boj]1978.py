def check(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
N = int(input())
arr = list(map(int, input().split()))
count = 0
for element in arr:
    if check(element):
        count += 1
    else:
        continue
print(count)