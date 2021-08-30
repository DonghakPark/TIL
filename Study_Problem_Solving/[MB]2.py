from collections import deque
def solution(a):
    answer = []

    for element in a:
        if element == "a":
            answer.append(True)
            continue
        if element.count("b")%2 != 0:
            answer.append(False)
            continue

        q = []
        q.append(element)
        while q:
            now_element = q.pop()

            if now_element == "a":
                answer.append(True)
                break

            while len(now_element) > 1:
                if now_element[0] != "a" and now_element[-1] != "a":
                    q.append(now_element)
                    break

                if now_element[0] == "a":
                    now_element = now_element[1:]
                elif now_element[-1] == "a":
                    now_element = now_element[:-1]

            if now_element[0] == "b" and now_element[-1] == "b":
                a_count = now_element.count("a")
                cnt_1 = now_element[:a_count].count("b")
                cnt_2 = now_element[-a_count:].count("b")
                if cnt_1 == cnt_2 and cnt_1 == a_count and now_element[a_count:-a_count] not in q:
                    q.append(now_element[a_count:-a_count])
                else:
                    answer.append(False)
                    break

    return answer

if __name__ == "__main__":
    print(solution(["abab", "bbaa", "bababa", "bbbabababbbaa"]),[True, False, False, True])
