from collections import defaultdict
import math


def solution(fees, records):
    answer = []

    record_dict = defaultdict(list)
    car_num = defaultdict(list)

    for element in records:
        now_time, now_car, now_statue = element.split()

        car_num[now_car] = [0, 0]

        convert_time = int(now_time.split(":")[0]) * 60 + int(now_time.split(":")[1])

        if now_statue == "IN":
            record_dict[now_car].append(convert_time)
        else:
            record_dict[now_car].append(convert_time)

    for key in record_dict.keys():
        if len(record_dict[key]) % 2 != 0:
            record_dict[key].append(1439)

        for i in range(0, len(record_dict[key]), 2):
            sum_time = record_dict[key][i + 1] - record_dict[key][i]
            car_num[key][0] += sum_time

    for key in car_num.keys():
        if car_num[key][0] <= fees[0]:
            car_num[key][1] = fees[1]
        else:
            now_fee = fees[1]
            last_time = math.ceil((car_num[key][0] - fees[0]) / fees[2])
            now_fee += last_time * fees[3]
            car_num[key][1] = now_fee

    unsorted_arr = []

    for key in car_num.keys():
        unsorted_arr.append([int(key), car_num[key][1]])

    unsorted_arr.sort()

    for element in unsorted_arr:
        answer.append(element[1])

    return answer


if __name__ == "__main__":
    print(solution([180, 5000, 10, 600],
                   ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                    "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]), [14600, 34400, 5000])
    print(solution([120, 0, 60, 591],
                   ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]), [0, 591])
    print(solution([1, 461, 1, 10], ["00:00 1234 IN"]), [14841])
