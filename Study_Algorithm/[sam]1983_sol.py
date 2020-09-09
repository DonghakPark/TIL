# 조교의 성적 매기기
# 총점 = 중간고사 (35%) + 기말고사 (45%) + 과제 (20%)
# [입력]
# 
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 
# 다음 줄부터 각 테스트 케이스가 주어진다.
# 
# 테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
# 
# 테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.

T = int(input())

for test_case in range(1, T+1):
    Student_Num, Student = map(int, input().split())
    arr1 = []
    Grade = 0
    Grade_Alph = ""
    for student_each in range(1, Student_Num+1):
        a, b, c = map(int, input().split())
        Sum = a*0.35 + b*0.45 + c*0.2
        arr1.append((student_each, Sum))
    arr1.sort(key=lambda x: x[1], reverse=True)

    for student_each in range(0, Student_Num):
        if arr1[student_each][0] == Student:
            Grade = student_each+1

    if(Grade<=Student_Num/10):
        Grade_Alph = "A+"
    elif(Grade<=Student_Num/10*2):
        Grade_Alph = "A0"
    elif (Grade <= Student_Num / 10 * 3):
        Grade_Alph = "A-"
    elif (Grade <= Student_Num / 10 * 4):
        Grade_Alph = "B+"
    elif (Grade <= Student_Num / 10 * 5):
        Grade_Alph = "B0"
    elif (Grade <= Student_Num / 10 * 6):
        Grade_Alph = "B-"
    elif (Grade <= Student_Num / 10 * 7):
        Grade_Alph = "C+"
    elif (Grade <= Student_Num / 10 * 8):
        Grade_Alph = "C0"
    elif (Grade <= Student_Num / 10 * 9):
        Grade_Alph = "C-"
    elif (Grade <= Student_Num / 10 * 10):
        Grade_Alph = "D0"

    print("#%d %s" %(test_case, Grade_Alph))


# 다른 사람 답
# import math
# T = int(input())
#  
# for t in range(1, T + 1):
#     n, m = map(int, input().split())
#     rank = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
#     scores = []
#     for i in range(n):
#         score = list(map(int, input().split()))
#         scores.append(round(score[0]*0.35 + score[1]*0.45 + score[2]*0.20, 3))
#  
#     student_score = scores[m-1]
#     scores.sort(reverse=True)
#     result = math.ceil((scores.index(student_score) + 1)*10/n)
#     print('#{} {}'.format(t, rank[result-1]))