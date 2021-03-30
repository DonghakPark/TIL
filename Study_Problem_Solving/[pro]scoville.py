import heapq

def check_answer(arr, k):
    for element in arr:
        if element < k:
            return False
        return True

def solution(scoville, K):
    heapq.heapify(scoville)
    time = 0

    while len(scoville) >= 2:
        if check_answer(scoville, K):
            return time
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = (first + (second * 2))
        heapq.heappush(scoville, new_scoville)
        time += 1
    if check_answer(scoville, K):
        return time
    else:
        return -1
