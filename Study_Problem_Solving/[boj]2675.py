tc = int(input())
for i in range(tc):
    R, S = input().split()
    R = int(R)
    S = list(S)
    answer = ''
    for j in range(len(S)):
        for k in range(R):
            answer += S[j]
    print(answer)

