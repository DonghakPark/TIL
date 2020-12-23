# def solution(food_times, k):
#     answer = 0
#     time = 0
#     thres = 0
#
#     iterate = k//len(food_times)
#     min_food_times = min(food_times)
#
#     if min_food_times >= iterate:
#         thres = iterate
#
#         time = iterate * len(food_times)
#
#     else:
#         thres = min_food_times
#
#         time = min_food_times * len(food_times)
#
#     result = 0
#     while time < k:
#
#         # 도중에 모든 음식을 먹었다면
#
#         if food_times.count(thres) == len(food_times):
#             return -1
#
#         if food_times[result] == thres:
#             result = (result + 1) % len(food_times)
#             continue
#         else:
#             food_times[result] -= 1
#             result = (result + 1) % len(food_times)
#             time +=1
#
#     while True:
#         if food_times[result] != thres:
#             break
#         else:
#             result = (result + 1) % len(food_times)
#
#     if food_times.count(thres) == len(food_times):
#         return -1
#     else:
#         return result +1

import heapq

def solution(food_times, k):
    # 다 먹는 경우
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, [food_times[i],i+1])

    total_time = 0
    length = len(food_times)


    while total_time + (q[0][0] * length) <= k:
        temp = heapq.heappop(q)[0]
        total_time += temp * length
        length -=1

        for i in range(len(q)):
            q[i][0] -= temp
    q.sort(key = lambda x: x[1])
    answer = q[(k-total_time)%length][1]
    return answer


# def solution(food_times, k):
#
#     #전체 음식을 먹는 시간보다 K가 크거나 같다면 -1
#     if sum(food_times) <= k:
#         return -1
#
#     q = []
#     for i in range(len(food_times)):
#         # 우선 순위 큐에 삽입 ( 음식 시간, 음식 번호 )
#         heapq.heappush(q, (food_times[i],i+1))
#
#     sum_value = 0 # 먹기 위해 사용한 시간
#     previous = 0 # 직전에 다 먹은 음식 시간
#
#     length = len(food_times) # 남은 음식의 갯수
#
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now-previous) * length
#         length -= 1
#         previous = now
#     result = sorted(q, key=lambda x:x[1])
#     return result[(k-sum_value) % length][1]

if __name__=="__main__":
    food_times = [4,2,3,6,7,1,5,8]
    k = 27
    print(solution(food_times, k))