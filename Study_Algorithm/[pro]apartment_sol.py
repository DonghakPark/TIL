import math
def solution(n, stations, w):
    answer = 0
    dist = []

    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1) - (stations[i-1]+w))

    dist.append(stations[0]-w-1)
    dist.append(n - (stations[-1] + w))

    for i in dist:
        try:
            answer += math.ceil(i / ((w*2) +1))
        except:
            continue
    return answer

if __name__=="__main__":
    N = 11
    stations = [4,11]
    w = 1
    print(solution(N,stations,w))
