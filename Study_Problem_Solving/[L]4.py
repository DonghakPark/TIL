def recursive_func(arr):
    global answer
    length = len(arr)

    if length == 1:
        answer.append(arr[0])
        return

    p = 0
    for i in range(2, length + 1):
        if length % i == 0:
            p = i
            break

    temps = [[] for _ in range(p)]

    for i in range(p):
        for j in range(length // p):
            temps[i].append(arr[(p * j) + i])

    for temp in temps:
        recursive_func(temp)

def solution(n):
    global answer

    answer = []
    arr = [i for i in range(1, n + 1)]

    recursive_func(arr)

    return answer


if __name__ == "__main__":
    print(solution(12), [1, 5, 9, 3, 7, 11, 2, 6, 10, 4, 8, 12])
    print(solution(18), [1, 7, 13, 3, 9, 15, 5, 11, 17, 2, 8, 14, 4, 10, 16, 6, 12, 18])
