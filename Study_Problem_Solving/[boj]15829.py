L = int(input())
S = input()
sum = 0
M = 1234567891
r = 31
i = 0
for element in S:
    temp = ord(element) - 96
    sum += temp * (r ** i)
    i += 1

answer = sum % M
print(answer)