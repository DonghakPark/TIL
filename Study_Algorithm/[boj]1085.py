x, y, w, h = map(int, input().split())
case1 = abs(w-x)
case2 = abs(h-y)
print(min(case1,case2,x,y))
