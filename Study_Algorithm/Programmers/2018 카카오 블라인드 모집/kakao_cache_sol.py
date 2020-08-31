def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer

    cache_arr = []

    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in cache_arr:
            answer += 1
            cache_arr.remove(cities[i])
            cache_arr.insert(0, cities[i])

        if cities[i] not in cache_arr:
            answer += 5
            cache_arr.insert(0, cities[i])

        if len(cache_arr) > cacheSize:
            cache_arr.pop()

    return answer

if __name__ == "__main__":
    cacheSize = 2
    cities = ["Jeju","Jeju","Jeju","Jeju","Jeju",]
    result = solution(cacheSize, cities)
    print(result)