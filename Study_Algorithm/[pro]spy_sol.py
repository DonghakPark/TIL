# def solution(clothes):
#     answer = 0
#
#     dic = {}
#
#     for element in clothes:
#         if element[1] not in dic:
#             dic[element[1]] = 1
#         else:
#             dic[element[1]] += 1
#
#     if len(dic) != 1:
#         answer = 1
#         for i in dic:
#             answer = answer * dic[i]
#
#     for i in dic:
#         answer = answer + dic[i]
#     return answer

from collections import Counter
from functools import reduce


def solution(clothes):

    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer

if __name__=="__main__":
    clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(clothes))