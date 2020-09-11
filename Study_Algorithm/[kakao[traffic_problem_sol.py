import datetime
import math

def solution2(lines):
    answer =0
    record = []

    for line in lines:
        temp = []

        hour = int(line.split()[1].split(':')[0]) * 3600
        min = int(line.split()[1].split(":")[1]) * 60
        sec = float(line.split()[1].split(":")[2])
        temp.append(round(hour+min+sec,3))
        temp.append(round( temp[0]+float(line.split()[2][:-1]),3 ) )

        record.append(temp)
    print(record)
    accumulated = 0
    max_requests = 1
    record.sort(key=lambda x: x[0])
    for i, elem1 in enumerate(record):
        current = accumulated

        for elem2 in record[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
        max_requests = max(max_requests, current)
        accumulated += elem1[1]

    answer = (max_requests)
    return answer


def solution(lines):
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

    print(combined_logs)

    accumulated = 0
    max_requests = 1
    combined_logs.sort(key=lambda x : x[0])
    print(combined_logs)
    
    for i, elem1 in enumerate(combined_logs):
        current = accumulated

        for elem2 in combined_logs[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
        max_requests = max(max_requests, current)
        accumulated += elem1[1]
    return max_requests


if __name__=="__main__":
    lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
    print(solution(lines))
    print(solution2(lines))