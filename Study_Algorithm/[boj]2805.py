import sys

N, M = map(int, sys.stdin.readline().split())
tree_h = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(tree_h)

while start <= end:
    mid = (start + end ) //2

    log = 0
    for i in tree_h:
        if i >= mid:
            log+= i-mid

    if log >= M:
        start = mid + 1
    else:
        end = mid-1
print(end)