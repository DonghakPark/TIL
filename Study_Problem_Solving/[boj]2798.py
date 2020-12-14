from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

combi = combinations(arr, 3)
combi = list(combi)

local_max = 0
for element in combi:
    local_sum = sum(element)
    if local_sum <= M:
        local_max = max(local_max, local_sum)

print(local_max)