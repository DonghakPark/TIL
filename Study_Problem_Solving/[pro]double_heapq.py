import heapq

def solution(operations):
    answer = []

    max_heap = []
    min_heap = []

    for command in operations:
        temp = list(command.split())
        if temp[0] == "I":
            heapq.heappush(min_heap, int(temp[1]))
            heapq.heappush(max_heap, -int(temp[1]))
        elif temp[0] == "D":
            if max_heap:
                if temp[1] == "1":
                    target = heapq.heappop(max_heap)
                    min_heap.remove(-target)
                    heapq.heapify(min_heap)
                else:
                    target = heapq.heappop(min_heap)
                    max_heap.remove(-target)
                    heapq.heapify(max_heap)
    if max_heap:
        answer.append(-int(heapq.heappop(max_heap)))
        answer.append(int(heapq.heappop(min_heap)))
    else:
        answer.append(0)
        answer.append(0)

    return answer