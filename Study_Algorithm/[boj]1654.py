K, N = map(int, input().split())
lan = []
for i in range(K):
    lan.append(int(input()))

start, end = 1, max(lan)

while start <= end:
    mid = (start+end)//2
    lines = 0
    for i in lan:
        lines += i // mid

    if lines >= N:
        start = mid+1
    else:
        end = mid-1
print(end)