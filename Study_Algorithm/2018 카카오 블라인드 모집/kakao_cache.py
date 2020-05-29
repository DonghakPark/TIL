def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    arr = [""] * cacheSize

    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in arr:
            answer += 1

        if cities[i] not in arr:
            answer += 5
            if cities[i] in arr:
                continue
            elif cities[i] not in arr:
                arr[i%cacheSize] = cities[i]

    return answer

if __name__ == "__main__":
    cacheSize = 0
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    result = solution(cacheSize, cities)
    print(result)