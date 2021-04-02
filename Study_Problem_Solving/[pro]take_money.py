def solution(money):

    dp_table1 = [0] * len(money)

    dp_table1[0] = money[0]
    dp_table1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1):
        dp_table1[i] = max(dp_table1[i-1], dp_table1[i-2] + money[i])

    dp_table2 = [0] * len(money)
    dp_table2[0] = 0
    dp_table2[1] = money[1]

    for i in range(2, len(money)):
        dp_table2[i] = max(dp_table2[i-1], dp_table2[i-2] + money[i])

    return max(max(dp_table1), max(dp_table2))

if __name__=="__main__":
    print(solution([1, 2, 3, 1]), 4)
    print(solution([1, 1, 4, 1, 4]), 8)
    print(solution([1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]), 3000)
    print(solution([1000, 1, 0, 1, 2, 1000, 0]), 2001)
    print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]), 2000)
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]), 201)
    print(solution([11, 0, 2, 5, 100, 100, 85, 1]), 198)
    print(solution([1, 2, 3]), 3)
    print(solution([91, 90, 5, 7, 5, 7]), 104)
    print(solution([90, 0, 0, 95, 1, 1]), 185)