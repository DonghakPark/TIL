list1 = []
for i in range(3):
    list1.append(int(input()))
answer = list1[0] * list1[1] * list1[2]
answer = list(str(answer))
for i in range(10):
    print(answer.count(str(i)))
