from itertools import combinations

def compare(arr1, arr2):

    list_arr1 = list(combinations(arr1, len(arr1) - 2))
    candidate_arr1 = []
    for element in list_arr1:
        candidate_arr1.append("".join(element))

    if arr2 in candidate_arr1:
        return True

    list_arr1 = list(combinations(arr1, len(arr1) - 1))
    list_arr2 = list(combinations(arr2, len(arr2) - 1))
    candidate_arr1 = []
    candidate_arr2 = []

    for element in list_arr1:
        candidate_arr1.append("".join(element))

    for element in list_arr2:
        candidate_arr2.append("".join(element))

    for element in candidate_arr1:
        for element2 in candidate_arr2:
            if element == element2:
                return True

    list_arr2 = list(combinations(arr2, len(arr2) - 2))
    candidate_arr2 = []
    for element in list_arr2:
        candidate_arr2.append("".join(element))

    if arr1 in candidate_arr2:
        return True

    return False

def solution(nicks, emails):
    answer = 0
    candidate_combi = list(combinations(nicks, 2))

    for element in candidate_combi:
        arr1, arr2 = element
        is_same = compare(arr1, arr2)
        if is_same:
            print(arr1, arr2, is_same)


    return answer

if __name__ == "__main__":
    print(solution(["imhero111", "moneyman", "hero111", "imher1111", "hro111", "moneyman", "moneymannnn"],
                   ["superman5@abcd.com", "batman432@korea.co.kr", "supterman@abcd.com","supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]), 3)

    print(solution(["99police", "99poli44"], ["687ufq698@aaa.xx.yyy", "87ufq687@aaa.xx.yyy"]), 2)

    print(solution(["99polico", "99policd"], ["687ufq687@aaa.xx.yyy", "587ufq687@aaa.xx.yyy"]), 2)

