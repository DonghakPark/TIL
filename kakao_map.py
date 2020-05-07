def solution(n, arr1, arr2):
    answer = []
    a12 = []
    for a,b in zip(arr1, arr2):
        answer = str(bin(a|b))[2:]
        answer = '0' * (n-len(answer))+answer
        answer = answer.replace("0"," ")
        answer = answer.replace("1","#")
        a12.append(answer)
    return a12

