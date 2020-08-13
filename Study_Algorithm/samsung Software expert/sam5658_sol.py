
T = int(input())

for test_case in range(1,T+1):
    N,K = map(int, input().split())
    num = list(input())

    answer = []

    #한변의 길이
    len_a = int(N/4)

    #4번 돌림
    for k in range(len_a):
        for i in range(4):
            temp = ''
            for j in range(len_a):
                temp += num[i*len_a + j]
            answer.append(int('0x'+temp, 16))

        num.append(num.pop(0))
    answer = set(answer)
    answer = list(answer)
    answer.sort(reverse=True)
    print("#{} {}".format(test_case, answer[K-1]))
