def solution(brown, yellow):
    x, y = brown // 2 - 1, 1

    while True:
        if (x - 2) * y == yellow:
            return [x, y + 2]
        x, y = x - 1, y + 1

if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
