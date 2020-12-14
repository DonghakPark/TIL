S = list(input())
answer = ''

for i in range(97, 123):
    if chr(i) in S:
        answer += str(S.index(chr(i)))
    else:
        answer += '-1'
    answer += ' '
print(answer)