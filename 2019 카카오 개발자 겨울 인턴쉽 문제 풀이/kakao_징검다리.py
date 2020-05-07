def solution(stones, k):
    answer = 0
    while True:
        if st(stones) == 1:
            return answer

        answer += 1
        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1

def st(stones):
    for i in range(0, len(stones)-2):
        if (stones[i] <=0 and stones[i+1] <= 0 and stones[i+2] <=0):
            return 1

if __name__=="__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    result = solution(stones, k)
    print(result)