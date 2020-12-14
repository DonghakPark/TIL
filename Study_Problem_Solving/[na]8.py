# 문자열 재정렬

S = list(input())

alpha = []

digit = []

for element in S:
    if element.isdigit():
        digit.append(int(element))
    elif element.isalpha():
        alpha.append(element)
    else:
        continue
alpha.sort()
sum = sum(digit)
answer = "".join(alpha) + str(sum)
print(answer)