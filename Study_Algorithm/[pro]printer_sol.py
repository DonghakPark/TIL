def solution(priorities, location):
    answer = 0

    while priorities:
        len_1 = len(priorities) #처음 길이

        temp = priorities.pop(0) #1개를 뽑아냄

        for element in priorities:
            if element > temp:
                priorities.append(temp)
                if location == 0:
                    location = len_1 -1
                else:
                    location = location -1
                break

        if len_1 != len(priorities):
            answer = answer + 1
            if location == 0:
                break
            else:
                location = location - 1
                continue

    return answer

if __name__ == "__main__":
    # priorities = [2,1,3,2]
    # location = 2
    # print(solution(priorities, location))

    priorities2 = [1,1,9,1,1,1]
    location2 = 0
    print(solution(priorities2, location2))
