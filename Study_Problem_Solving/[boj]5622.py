"""
다이얼 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

arr = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

S = input()
answer = 0
for char in S:
    answer += arr[ord(char) - 65]
print(answer)
