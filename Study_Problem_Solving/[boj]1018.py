def compare(a,b):
    if len(a) != len(b):
        return
    else:
        diff = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                continue
            else:
                diff += 1
        return diff

R,L = map(int, input().split())
board = []
for i in range(R):
    temp = list(input())
    board.append(temp)


case1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
case2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

new_R = R - 7
new_L = L - 7


answer = 2e9

for i in range(new_R):

    for j in range(new_L):
        count1 = 0
        count2 = 0
        for k in range(8):
            temp = board[i+k][j:j+8]
            if k%2 == 0:
                count1 += compare(temp, case1)
                count2 += compare(temp, case2)
            else:
                count1 += compare(temp, case2)
                count2 += compare(temp, case1)
        min_local = min(count1,count2)
        answer = min(min_local,answer)
print(answer)
