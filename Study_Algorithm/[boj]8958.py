tc = int(input())
for i in range(tc):
    A = input()
    count = 0
    answer = 0
    for j in range(len(A)):
        if A[j] =="O":
            count += 1
            answer += count
        else:
            count = 0
    print(answer)