def solution(answers):
    answer = []

    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]

    cnt_1, cnt_2, cnt_3 = 0,0,0

    for i in range(0,len(answers)):
        if answers[i] == student1[i%5]:
            cnt_1 += 1
        if answers[i] == student2[i%8]:
            cnt_2 += 1
        if answers[i] == student3[i%10]:
            cnt_3 += 1

    cnt = []
    cnt.append([cnt_1,1])
    cnt.append([cnt_2, 2])
    cnt.append([cnt_3, 3])

    cnt.sort(reverse = True)
    max = cnt[0][0]
    for element in cnt:
        if element[0] == max:
            answer.append(element[1])

    answer.sort()
    return answer

if __name__=="__main__":
    answers1 = [1,2,3,4,5]
    answers2 = [1,3,2,4,2]

    print(solution(answers1))
    print(solution(answers2))
