from itertools import permutations, product
def solution(dice):
    answer = 0
    N = len(dice)
    permu_list = []
    candidate_list = []
    for i in range(1,N+1):
        permu_list.append(list(permutations(dice, i)))

    for element in permu_list:

        for element2 in element:
            product_num = list(product(*element2))
            for element3 in product_num:
                candidate_list.append(int("".join(map(str, element3))))

    candidate_list = set(candidate_list)

    for i in range(1,10000):
        if i not in candidate_list:
            answer = i
            return answer

if __name__ == "__main__":
    print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]), 22)
    print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]), 66)

