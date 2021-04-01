"""

def solution(N, number):
    answer = 0
    dp_table = [int(1e9)] * ((number * N) + 1)
    visited = [False] * ((number * N) + 1)
    Q = []

    dp_table[N] = 1
    Q.append(N)

    now = N
    count = 1
    N_list = [N]

    while True:

        if int(str(now) + str(N)) > (number * N):
            break
        else:
            now = int(str(now) + str(N))
            count += 1
            Q.append(now)
            dp_table[now] = count
            visited[now] = True
            N_list.append(now)
    while Q:
        now_num = Q.pop(0)

        new_num = []
        for element in N_list:
            new_num.append(now_num + element)
            new_num.append(now_num - element)
            new_num.append(now_num * element)
            new_num.append(now_num // element)

        for element in new_num:

            if 0 <= element < (len(visited)):
                if visited[element] is False:
                    dp_table[element] = min(dp_table[element], dp_table[now_num] + 1)
                    Q.append(element)
                    visited[element] = True

    answer = dp_table[number]

    if answer > 8:
        return -1
    else:
        return answer
"""

def solution(N, number):
    if N == number:
        return 1
    answer = - 1
    S = [set() for x in range(8)]
    for i,x in enumerate(S, start = 1):
        x.add(int(str(N) * i))
    for i in range(1, len(S)):
        for j in range(i):
            for op1 in S[j]:
                for op2 in S[i-j-1]:
                    S[i].add(op1 + op2)
                    S[i].add(op1 - op2)
                    S[i].add(op1 * op2)
                    if op2 != 0:
                        S[i].add(op1 // op2)
        if number in S[i]:
            answer = i + 1
            break
    return answer

if __name__ == "__main__":
    N = 5
    number = 12
    print(solution(N, number))
