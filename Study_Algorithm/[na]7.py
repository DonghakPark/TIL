#럭키 스트라이크 문제

N = list(map(int,input()))

left = 0
right = 0

for i in range(0,int(len(N)/2)):
    left += N[i]

for i in range(int(len(N)/2), len(N)):
    right += N[i]

if left == right:
    print("LUCKY")
else:
    print("READY")