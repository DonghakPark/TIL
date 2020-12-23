"""
모험가 길드
author : donghak park
contact : donghark03@naver.com
"""
N = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
answer = 0

while True:
    if len(arr)==0:
        break

    temp = arr.pop(0)

    #공포도 보다 남은 사람수가 적을 경우
    if temp-1 > len(arr):
        break

    else:
        answer += 1
        for i in range(temp-1):
            arr.pop()

print(answer)

"""
책 풀이 
"""
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# result = 0 #총 그룹의 수
# count = 0  #현재 그룹에 포함된 모험가의 수
#
# for i in data: #공포도를 낮은 것부터 하나씩 확인하며
#     count += 1 #현재 그룹에 해당 모험가를 포함시키기
#     if count >= i:
#         result += 1
#         count = 0
# print(result)
