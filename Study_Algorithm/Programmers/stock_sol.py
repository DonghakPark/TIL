def solution(prices):
    answer = []

    for j in range(0, len(prices)):

        count = 0

        for i in range(j+1, len(prices)):
            if prices[i] >= prices[j]:
                count += 1
            else:
                count += 1
                break

        answer.append(count)

    return answer


if __name__=="__main__":
    prices = [1,2,3,2,3]
    print(solution(prices))