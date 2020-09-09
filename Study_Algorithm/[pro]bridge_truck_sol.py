def solution(bridge_length, weight, truck_weights):
    answer = 0
    Queue = [0] * bridge_length
    time = 0
    while Queue:
        time += 1
        Queue.pop(0)
        if truck_weights:
            if sum(Queue) + truck_weights[0] <= weight:
                Queue.append(truck_weights.pop(0))
            else:
                Queue.append(0)
    answer = time

    return answer

if __name__=="__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    print(solution(bridge_length, weight, truck_weights))
