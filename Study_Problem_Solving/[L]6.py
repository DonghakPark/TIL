from collections import defaultdict
from collections import Counter


def converter(date):
    temp = list(map(int, date.split("-")))
    ret = (temp[1] - 1) * 30 + temp[2]
    return ret


def solution(records, k, date):
    total_dict = defaultdict(list)
    set_dict = defaultdict(set)

    answer = []
    new_records = []

    for record in records:
        now_date, uid, pid = record.split()
        new_date = converter(now_date)
        base = converter(date)
        new_records.append([base - new_date, int(uid[3:]), int(pid[3:])])

    for record in new_records:
        if 0 <= record[0] <= k - 1:
            set_dict[record[2]].add(record[1])
            total_dict[record[2]].append(record[1])

    unsorted_arr = []

    for key in set_dict.keys():
        count = Counter(total_dict[key])
        total_count = len(total_dict[key])
        numerator, denominator = 0, len(set_dict[key])

        for count_key in count.keys():
            if count[count_key] > 1:
                numerator += 1

        unsorted_arr.append([(numerator / denominator) * 100, total_count, key])

    unsorted_arr.sort(key=lambda x: (-x[0], -x[1], x[2]))

    if len(unsorted_arr) == 0:
        answer.append("no result")
    else:
        for arr in unsorted_arr:
            answer.append("pid" + str(arr[2]))

    return answer


if __name__ == "__main__":
    print(solution(["2020-02-02 uid1 pid1", "2020-02-26 uid1 pid1", "2020-02-26 uid2 pid1", "2020-02-27 uid3 pid2",
                    "2020-02-28 uid4 pid2", "2020-02-29 uid3 pid3", "2020-03-01 uid4 pid3", "2020-03-03 uid1 pid1",
                    "2020-03-04 uid2 pid1", "2020-03-05 uid3 pid2", "2020-03-05 uid3 pid3", "2020-03-05 uid3 pid3",
                    "2020-03-06 uid1 pid4"], 10, "2020-03-05"), ["pid1", "pid3", "pid2"])
    print(solution(
        ["2020-02-02 uid141 pid141", "2020-02-03 uid141 pid32", "2020-02-04 uid32 pid32", "2020-02-05 uid32 pid141"],
        10, "2020-02-05"), ["pid32", "pid141"])
    print(solution(["2020-01-01 uid1000 pid5000"], 10, "2020-01-11"), ["no result"])
