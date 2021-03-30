import heapq


def solution(jobs):
    answer = 0
    jobs.sort()
    N = len(jobs)

    Q = []
    HW = 0
    time = 0
    total_time = 0
    while True:
        if len(Q) == 0 and len(jobs) == 0:
            break

        if jobs:
            if jobs[0][0] <= time:
                start_time, task_time = jobs.pop(0)
                heapq.heappush(Q, [task_time, start_time])

        if HW == 0:
            if Q:
                take_time_pop, start_time_pop = heapq.heappop(Q)
                total_time += time + take_time_pop - start_time_pop
                HW += take_time_pop -1
        else:
            HW -= 1
        time += 1

    answer = (total_time) // N

    return answer

if __name__=="__main__":
    jobs = [[0,3], [1,9],[2,6]]
    print(solution(jobs))