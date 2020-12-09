import math
n, r = map(int, input().split())

result = math.factorial(n) /(math.factorial(r) * (math.factorial(n-r)) )
print(int(result))