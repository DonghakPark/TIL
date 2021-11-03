def solution(enter, leave):
    answer = [0] * (len(enter) + 1)

    for idx in range(len(enter)):

        idx_in = idx
        in_front = set(enter[:idx_in])
        in_rear = set(enter[idx_in + 1:])

        idx_out = leave.index(enter[idx])
        out_front = set(leave[:idx_out])
        out_rear = set(leave[idx_out + 1:])

        rear_front = in_rear & out_front
        front_rear = in_front & out_rear

        rear_rear = in_rear & out_rear
        front_front = in_front & out_front

        candidate = set()

        for element in rear_rear:
            element_idx_in = enter.index(element)
            temp_set = set(enter[element_idx_in + 1:])
            if out_front & temp_set:
                candidate.add(element)

        for element in front_front:
            element_idx_out = leave.index(element)
            temp_set = set(leave[:element_idx_out])
            if in_rear & temp_set:
                candidate.add(element)

        total = set()
        total = total | rear_front
        total = total | front_rear
        total = total | candidate

        answer[enter[idx]] += len(total)

    return answer[1:]

def solution2(enter, leave):
    answer = [[] for _ in range(len(enter) + 1)]
    room = []
    ei, li = 0, 0
    while ei < len(enter) or li <len(leave):
        if leave[li] not in room:
            answer[enter[ei]] = room[:]
            room.append(enter[ei])
            ei += 1
        else:
            room.remove(leave[li])
            li += 1
    for p, person in enumerate(answer):
        for met in person:
            answer[met].append(p)
    return [len(set(i)) for i in answer][1:]

if __name__ == "__main__":
    print(solution([1, 3, 2], [1, 2, 3]), [0, 1, 1])
    print(solution([1, 4, 2, 3], [2, 1, 3, 4]), [2, 2, 1, 3])
    print(solution([3, 2, 1], [2, 1, 3]), [1, 1, 2])
    print(solution([3, 2, 1], [1, 3, 2]), [2, 2, 2])
    print(solution([1, 4, 2, 3], [2, 1, 4, 3]), [2, 2, 0, 2])
    print(solution([1, 2, 3], [3, 2, 1]), [2, 2, 2])
