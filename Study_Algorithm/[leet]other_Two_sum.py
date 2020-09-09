def solution(nums, target):
    lookup = {}
    for cnt, num in enumerate(nums):
        if target-num in lookup:
            return lookup[target-num], cnt
        lookup[num] = cnt

if __name__=="__main__":
    nums = [2,7,11,15]
    target = 9
    print(solution(nums, target))
