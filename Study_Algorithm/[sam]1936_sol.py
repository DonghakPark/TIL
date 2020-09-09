# 가위 = 1 바위 =2 보 =3
A,B = map(int, input().split())
ans = ""
if A>B and A!=3:
    ans = "A"
elif A==3 and B!=1:
    ans = "A"
else:
    ans = "B"
print(ans)