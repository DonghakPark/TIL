def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            answer = p
            return answer
    answer = participant[-1]
    return answer

if __name__=="__main__":
    participant1 = ["leo", "kiki", "eden"]
    participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
    participant3 = ["mislav", "stanko", "mislav", "ana"]

    completion1 = ["eden", "kiki"]
    completion2 = ["josipa", "filipa", "marina", "nikola"]
    completion3 = ["stanko", "ana", "mislav"]

    print(solution(participant1, completion1))
    print(solution(participant2, completion2))
    print(solution(participant3, completion3))