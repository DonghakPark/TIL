def solution(heights):
    len_h = len(heights)
    answer = [0] * len_h

    for i in range(1, len_h+1):
        for j in range(i+1,len_h+1):
            if heights[-j] > heights[-i]:
                answer[-i] = len_h - j +1
                break;

    return answer

if __name__ == "__main__":
    heights = [6,9,5,7,4]
    print(solution(heights))

    heights2 = [3, 9, 9, 3, 5, 7, 2]
    print(solution(heights2))

    heights3 = [1, 5, 3, 6, 7, 6, 5]
    print(solution(heights3))