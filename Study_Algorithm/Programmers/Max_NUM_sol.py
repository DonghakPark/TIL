def solution(numbers):
    numbers = list(map(str, numbers))
    answer = "".join(sorted(numbers, key=lambda x: (x[0], x[1%len(x)], x[2%len(x)], x[3%len(x)]),reverse=True))

    return answer if int(answer) != 0 else "0"

if __name__=="__main__":
    numbers = [6,10,2]
    print(solution(numbers))