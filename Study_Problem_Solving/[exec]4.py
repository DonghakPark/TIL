from collections import defaultdict


def solution(param0):
    answer = []

    counting_dict = defaultdict(list)
    order = 1
    while param0:
        now_path = param0.pop(0)

        # 디렉토리 정보 모두 제거
        now_file = now_path.split("/")[-1]

        # 버전 정보가 있으면 제거
        cleared_file_name = now_file[0] + now_file[-2:]

        # 처음 나왔으면
        if cleared_file_name not in counting_dict.keys():
            counting_dict[cleared_file_name] = [order, 1]
            order += 1
        else:
            counting_dict[cleared_file_name][1] += 1

    new_list = []

    for key in counting_dict.keys():
        if counting_dict[key][1] >= 2:
            new_list.append([counting_dict[key][0], key, counting_dict[key][1]])

    new_list.sort(key=lambda x: x[0])

    for element in new_list:
        answer.append(element[1])
        answer.append(str(element[2]))

    return answer
