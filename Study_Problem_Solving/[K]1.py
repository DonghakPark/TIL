from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    sum_report = defaultdict(int)
    who_report = defaultdict(list)
    cnt_report = defaultdict(int)

    report_list = []
    for element in report:
        from_report, to_report = element.split()
        report_list.append([from_report, to_report])

    for element in report_list:
        if element[0] not in who_report[element[1]]:
            who_report[element[1]].append(element[0])
            sum_report[element[1]] += 1

    for key in sum_report.keys():
        if sum_report[key] >= k:
            for element in who_report[key]:
                cnt_report[element] += 1

    for name in id_list:
        answer.append(cnt_report[name])

    return answer


if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2), [2, 1, 1, 0])
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3), [0, 0])
