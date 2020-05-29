def solution(s):
    answer = []
    arr = []
    s = s.replace("{{", "")
    s = s.replace("}}", "")
    s = s.split("},{")
    for i in s:
        i = list(map(int, i.split(",")))
        arr.append(i)
    for i in range(len(arr)):
        for j in arr:
            if len(j) == i+1:
                for element in j:
                    if element not in answer:
                        answer.append(element)

    return answer

if __name__ == "__main__":
    s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    result = solution(s)
    print(result)