"""
def solution(k, room_number):
    answer = []
    arr = []
    for i in range(1, k+1):
        arr.append(i)

    for req in room_number:
        if req in arr:
            answer.append(req)
            arr.remove(req)
        else:
            answer.append(near(arr,req))
    return answer

def near(arr, req):
    ans = 0
    for i in range(len(arr)):
        if arr[i] >= req:
            ans = arr[i]
            arr.remove(arr[i])
            return ans
"""

"""    arr = [0] * k
    for req in room_number:
        if arr[req-1] == 0:
            arr[req-1] = 1
            answer.append(req)
        else:
            for i in range(req-1, k):
                if arr[i] == 0:
                    arr[i] = 1
                    answer.append(i+1)
                    break
정확도 78.8 효율성 0 = 78.8
"""
def solution(k, room_number):
    room_dic = {}
    ret = []
    for i in room_number:
        n = i
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        ret.append(n)
        for j in visit:
            room_dic[j] = n+1
    return ret

if __name__ =="__main__":
    k = 10
    room_number =[1,3,4,1,3,1]
    result = solution(k, room_number)
    print(result)
