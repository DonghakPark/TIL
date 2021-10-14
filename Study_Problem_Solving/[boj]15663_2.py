import sys
input = sys.stdin.readline

temp = []

def solution(N, M, arr, answer, visited):

    if M == 0:
        temp.append(tuple(answer))
        return

    for i in range(N):
        if i in visited:
            continue
        else:
            answer.append(arr[i])
            visited.append(i)
            solution(N, M-1, arr, answer, visited)
            visited.pop()
            answer.pop()

if __name__ == "__main__":

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    solution(N, M, arr, [], [])

    answer = sorted(list(set(temp)))

    for element in answer:
        print(*element)