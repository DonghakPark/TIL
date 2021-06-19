import copy

def upperbound_binary_search(topping_list, now_cost, max_cost):
    left = 0
    right = len(topping_list) - 1

    while left < right:
        mid = (right + left) // 2
        if now_cost + topping_list[mid] <= max_cost:
            left = mid + 1
        else:
            right = mid

    return left

def solution(M, burger_list, topping_list):
    answer = 0
    burger_list.sort()
    topping_list.sort()

    max_answer = 0
    now_burger = 0

    len_burger = len(burger_list)

    while now_burger < len_burger:
        if burger_list[now_burger] > M:
            now_burger += 1
            continue

        temp_cost = burger_list[now_burger]

        res = upperbound_binary_search(topping_list, temp_cost, M)
        if temp_cost + topping_list[res] <= M:
            max_answer = max(max_answer, temp_cost + topping_list[res])
            new_topping = copy.deepcopy(topping_list)
            new_topping.pop(res)

            temp_cost = temp_cost + topping_list[res]

            res2 = upperbound_binary_search(new_topping, temp_cost, M)
            if temp_cost + new_topping[res2] <= M:
                max_answer = max(max_answer, temp_cost + new_topping[res2])

        else:
            max_answer = max(max_answer, temp_cost)

        now_burger += 1

    answer = max_answer
    if answer == 0:
        return -1

    return answer

if __name__=="__main__":
    print(solution(23, [8,20], [5,10]), 23)
    print(solution(1,[2,3],[4,5]),-1)
