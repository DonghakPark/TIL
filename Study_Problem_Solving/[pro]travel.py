from collections import defaultdict, deque


def DFS(Stack, visited, tickets):
    global answer

    if visited.count(True) == len(tickets):
        temp = []
        for element in Stack:
            temp.append(element)
        answer = temp
        return

    for i in range(len(tickets)):
        if visited[i] is False and tickets[i][0] == Stack[-1]:
            visited[i] = True
            Stack.append(tickets[i][1])
            DFS(Stack, visited, tickets)
            Stack.pop()
            visited[i] = False


answer = []


def solution(tickets):
    global answer
    answer = []
    visited = [False] * len(tickets)
    tickets.sort(key=lambda x: (x[1]))
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visited[i] = True
            DFS(["ICN", tickets[i][1]], visited, tickets)
            visited[i] = False

    return answer


if __name__ == "__main__":
    tickets = [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

    print(solution(tickets))
    print(solution(tickets2))
