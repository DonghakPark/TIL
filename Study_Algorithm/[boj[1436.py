N = int(input())
count = 0
start = 0
while True:
    start = int(start)
    start += 1
    start = str(start)
    if '666' in start:
        count += 1
        if count == N:
            print(start)
            break
