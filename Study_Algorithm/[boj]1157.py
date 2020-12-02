# S = list(input().upper())
#
# S2 = set(S)
# answer = []
# while S2:
#     temp = S2.pop()
#     answer.append([S.count(temp),temp])
#
# answer.sort(reverse=True)
#
# if answer[0][0] == answer[1][0]:
#     print("?")
# else:
#     print(answer[0][1])

words = input().lower()
words_list = list(set(words))
word_count = list()

for i in words_list:
    count = words.count(i)
    word_count.append(count)

if(word_count.count(max(word_count)) >= 2):
    print('?')
else:
    print(words_list[(word_count.index(max(word_count)))].upper())