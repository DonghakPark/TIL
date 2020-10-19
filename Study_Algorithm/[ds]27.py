N, K = map(int, input().split())

floor = []
person = [0] * N

floor = list(map(int, input().split()))

def move():
    global floor
    global person

    temp = floor.pop()
    floor.insert(0, temp)

    temp2 = person.pop()

    if temp2 == 1:
        temp2 = 0

    person.insert(0, temp2)

time = 1

while True:

    move()
    if person[-1] == 1:
        person[-1] = 0

    for i in range(N-1, -1, -1):
        x = i
        nx = i + 1

        #벨트 위에 사람이 없다면
        if person[x] == 0:
            continue
        # 벨트 위에 사람이 있다면
        else:
            if person[nx] == 0 and floor[nx] >= 1:
                person[x] = 0
                person[nx] = 1
                floor[nx] -= 1

        if person[-1] == 1:
            person[-1] = 0

    if floor[0] >= 1:
        person[0] = 1
        floor[0] -= 1

    count = 0
    for element in floor:
        if element == 0:
            count += 1

    if count >= K:
        break
    time += 1

print (time)

