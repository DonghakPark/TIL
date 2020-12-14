# # 이차원 배열과 연산

from _collections import Counter

r,c,k = map(int, input().split())
A = [list(map(int, input().split()) for _ in range(3)) ]

r = r-1 # 0index
c = c-1
time = 0

while time <= 100:
    if r<len(A) and c<len(A[0]) and A[r][c]==k:
        print(time)
        break

    #C연산인 경우 : Transpose
    C_flag = False
    if len(A) < len(A[0]):
        C_flag = True
        A=list(zip(*A))

    # row에 대한 주어진 연산 구현
    max_len = 0
    tmp_a = []
    for now_row in A:
        ct = Counter(now_row)
        if ct.get(0):
            del ct[0]
        num_cnt = list(map(list, ct.items()))
        num_cnt.sort(key = lambda x : (x[1],x[0]))
        tmp_a.append(list(sum(num_cnt, []))[:100])
        max_len = max(max_len, len(tmp_a[-1]))

        for i in range(len(tmp_a)):
            if len(tmp_a[i]) < max_len:
                tmp_a[i]+=[0]*(max_len - len(tmp_a[i]))

        A = tmp_a

        if C_flag:
            A = list(zip(*A))
        time += 1

    if time>100:
        print(-1)