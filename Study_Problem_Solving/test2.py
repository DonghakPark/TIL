import re

def solution(line1, line2):
    answer = 0
    element_list = list(line2)

    iterate_num = 0

    while True:

        now_pattern = ""

        for index_element in range(0, len(element_list)):
            now_pattern = now_pattern + element_list[index_element]

            if index_element != len(element_list) - 1 :
                for _ in range(iterate_num):
                    now_pattern = now_pattern + "."

        p = re.compile(now_pattern)
        for i in range(0, len(line1) - len(now_pattern)+1):
            result = p.findall(line1[i:i + len(now_pattern)])

            if result:
                answer += 1

        iterate_num += 1

        if len(now_pattern) > len(line1):
            break

    return answer
