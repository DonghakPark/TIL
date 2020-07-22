def solution(n, computers):
    answer = 0

    visit = [False] * n

    Q = list()

    for idx in range(n):

        if visit[idx] == False:
            visit[idx] = True
            Q.append(idx)

            while Q:

                temp = Q.pop(0)
                for net in range(n):

                    if computers[temp][net] == 1 and visit[net] == False:
                        visit[net] = True
                        Q.append(net)

            answer += 1

    return answer

if __name__=="__main__":

    n  =3
    computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    print(solution(n, computers))
