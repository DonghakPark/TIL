import math


def converter(num, target):
    ret = ''
    while num > 0:
        num, mod = divmod(num, target)
        ret += str(mod)

    return ret[::-1]


def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True


def solution(n, k):
    answer = 0

    new_num = converter(n, k)
    p_list = new_num.split('0')

    for element in p_list:
        if element == "" or element == "1":
            continue
        elif is_prime(int(element)):
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution(437674, 3), 3)
    print(solution(110011, 10), 2)
