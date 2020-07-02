def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(0,len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            count = 0
            while True:
                i =0

                if len(progresses) == 0:
                    break
                elif progresses[i] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    count += 1
                else:
                    break
            answer.append(count)

    return answer

if __name__=="__main__":
    progresses = [93,30,55]
    speeds = [1,30,5]

    print(solution(progresses, speeds))