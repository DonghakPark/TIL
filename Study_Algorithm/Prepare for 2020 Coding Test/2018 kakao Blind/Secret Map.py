def solution(n, arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        temp = bin(a1|a2)[2:]
        zeros = '0' * (n-len(temp))

        temp = zeros + temp

        temp2 = ''
        for s in temp:
            if s == '1':
                temp2 += '#'
            else:
                temp2 += " "

        answer.append(temp2)

    return answer

if __name__ =="__main__":
    n = 5
    arr1 = [9,20,28,18,11]
    arr2 = [30,1,21,17,28]
    print(solution(n,arr1,arr2))
