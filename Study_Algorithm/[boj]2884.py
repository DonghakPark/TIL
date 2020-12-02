h,m = map(int, input().split())
answer = h*60 + m
answer -= 45
H = answer//60
if H < 0:
    H = 24 + H
print("{} {}".format(H, answer%60))