import collections

def solution(numbers, target):
    answer = 0
    stack = collections.deque( [ (0,0) ] )
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))

    return answer


if __name__=="__main__":
    numbers = [1,1,1,1,1]
    target = 3
    print(solution(numbers, target))
