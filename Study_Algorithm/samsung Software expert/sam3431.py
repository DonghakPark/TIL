# 최근 경도비만 판정을 받은 준환이는 적절한 몸을 유지하기 위하여 1주일에 L분 이상 U분 이하의 운동을
# 하여야 한다.
# 준환이는 이번 주에 X분만큼 운동을 하였다.
# 당신은 준환이가 제한되어 있는 시간을 넘은 운동을 할 것인지, 그것이 아니라면 몇 분 더 운동을 해야 제한을
# 맞출 수 있는지 출력하는 프로그램을 작성해야한다.

T = int(input())
for test_case in range(1, T+1):
    L, U, X = map(int, input().split())
    ans = 0
    if X > U:
        ans = -1
    elif X < L:
        ans = L-X
    elif X >= L and X <= U:
        ans = 0
    print("#%d %d" %(test_case, ans) )
