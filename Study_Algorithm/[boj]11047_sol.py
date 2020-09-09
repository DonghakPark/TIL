# 준규가 가지고 있는 동전은 총 N 종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())
arr = []
for element in range(1, N+1):
    arr.append(int(input()))
arr.sort(reverse=True)
sum = 0
ans = 0
i = 0
while(K!=sum):
    if K == 0:
        break
    elif sum+arr[i] <= K :
        sum = sum + arr[i]
        ans = ans +1
    else:
        i = i+1

print(ans)

# n, k = map(int, input().split())
# m = []
# num = 0
# for i in range(n):
#     m.append(int(input()))
# for i in range(n - 1, -1, -1):
#     if k == 0:
#         break
#     if m[i] > k:
#         continue
#     num += k // m[i]
#     k %= m[i]
# print(num)
