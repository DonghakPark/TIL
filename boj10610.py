N = input()
N = sorted(N, reverse = True)
sum =0
if '0' not in N:
    print(-1)
else:
    for element in N:
       sum = sum + int(element)
    if (sum%3!=0):
        print(-1)
    else:
        print(''.join(N))
