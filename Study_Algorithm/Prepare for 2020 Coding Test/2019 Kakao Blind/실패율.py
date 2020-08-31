def solution(N, stages):
    answer = []
    N_list = [0] * (N+1)
    thr_list = [0] * (N+1)
    for user in stages:
        if user == N+1:
            for i in range(1, N+1):
                thr_list[i] += 1
            continue
        else:
            N_list[user] += 1

        for i in range(1,user+1):
            thr_list[i] += 1

    for i in range(1, N+1):
        answer.append(N_list[i]/thr_list[i])

    return answer

if __name__=="__main__":
    N1 = 5
    N2 = 4
    stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
    stages2 = 	[4,4,4,4,4]

    print(solution(N1, stages1))
    print(solution(N2, stages2))