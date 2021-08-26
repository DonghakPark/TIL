def solution(lines):
    answer = 0
    new_format_line = []

    for line in lines:
        end_time, take_time = line.split()[1:]  # 00:00:00.000, 3s
        time1, time2 = end_time.split(".")  # 00:00:00, 000
        time1 = list(map(int, time1.split(":"))) #[h,m,x]
        time2 = int(time2) #ms
        take_time = float(take_time[:-1]) * 1000 #convert to ms

        last_time = (time1[0] * 60 * 60 * 1000) + (time1[1] * 60 * 1000) + (time1[2] * 1000) + time2 #convert to ms
        first_time = last_time - take_time + 1 # calculate first time

        new_format_line.append([last_time, -1])
        new_format_line.append([first_time, 1])

    temp_answer = 0
    max_answer = 1
    new_format_line.sort(key=lambda x: x[0])

    for index, element in enumerate(new_format_line):
        now = temp_answer

        for element2 in new_format_line[index:]:
            if element2[0] - element[0] > 999:
                break
            if element2[1] > 0:
                now += 1

        max_answer = max(max_answer, now)
        temp_answer += element[1]

    answer = max_answer
    return


if __name__ == "__main__":
    # print(solution(["2016-09-15 00:00:00.000 3s"]), 1)
    # print(solution(["2016-09-15 23:59:59.999 0.001s"]), 1)
    # print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]), 1)
    print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]), 2)
    # print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s",
    #                 "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
    #                 "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s",
    #                 "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]), 7)
    # print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]), 1)
