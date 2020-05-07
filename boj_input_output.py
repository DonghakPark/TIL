# print("Hello World!")

# a,b = map(int, input().split())
# print(a+b)

# a = int(input())
# b = int(input())
# print(a+b)

# T = int(input())
# for test_case in range(1,T+1):
#     a,b = map(int, input().split())
#     print(a+b)

# while True:
#     try:
#         a,b = map(int, input().split())
#         print(a + b)
#     except:
#         break

# while True:
#     a,b = map(int, input().split())
#     if(a ==0 and b==0):
#         break;
#     print(a+b)

# T = int(input())
# for test_case in range(1, T+1):
#     A = input()
#     A = A.split(",")
#     A = list(map(int,A))
#     print(A[0]+A[1])

# T = int(input())
# for test_case in range(1, T+1):
#     a,b = map(int, input().split())
#     print("Case #%d: %d + %d = %d" %(test_case,a,b, a+b))

# while (True):
#     try:
#         T = input()
#         print(T)
#     except:
#         break

# T = input()
# sum =0
# a = input()
# a = list(map(int,a))
# for i in a:
#     sum = sum +i
# print(sum)

# S = input()
# T = ""
# for i in range(1, len(S)+1):
#     T = T + S[i-1]
#     if(i%10 == 0):
#         print(T)
#         T = ""
# print(T)

# T = int(input())
# for i in range(1,T+1):
#     print(i)

# T = int(input())
# for element in range(1, 10):
#     print("%d * %d = %d" %(T, element, T*element))

#달력 문제
# x,y = map(int, input().split())
# m31 = [3,5,7,10,12]
# m30 = [4,6,9,11]
#
# for i in range(1, x):
#     if i in m31:
#         y= y+31
#     elif i in m30:
#         y = y+30
#     elif i == 2:
#         y =y +28
#     elif x == 1:
#         continue
#
# if y%7 == 1:
#     print("MON")
# elif y%7 == 2:
#     print("TUE")
# elif y%7 == 3:
#     print("WED")
# elif y%7 == 4:
#     print("THU")
# elif y%7 == 5:
#     print("FRI")
# elif y%7 == 6:
#     print("SAT")
# elif y%7 == 0:
#     print("SUN")

# T = int(input())
# sum = 0
# for i in range(1,T+1):
#     sum = sum+i
# print(sum)

# a = input()
# T = input()
# T = list(map(int, T.split(" ")))
# print("%d %d" %(min(T), max(T)))

# T = int(input())
# for i in range(1, T+1):
#     s = "*"*i
#     print(s.rjust(T) )

# T = int(input())
# for i in range(1,T+1):
#     j = "*"*((i*2)-1)
#     print(j.center(T*2-1))
#
# T = int(input())
# for i in range(1,T+1):
#     S = "*"*i
#     print(S.rjust(T))
# for j in range(1, T):
#     S = "*"*(T-j)
#     print(S.rjust(T))

# N = int(input())
#
# for i in reversed(range(1, N+1)):
#     print(' ' * (N - i) + "*" * (2 * i-1))
# for i in range(2, N+1):
#     print(' ' * (N - i) + "*" * (2 * i - 1))

table = [(1,1,1), (1,1,1), (1,1,1)]
s =sum(table[a][b] for a in range(3) for b in range(3))
print(s)