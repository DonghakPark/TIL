# def solution(tickets):
# #     answer = []
# #
# #     candidate = ['ICN']
# #
# #     while candidate:
# #         temp = []
# #         temp2 = []
# #         start = candidate.pop(0)
# #         answer.append(start)
# #
# #         while tickets:
# #             ticket = tickets.pop(0)
# #
# #             if ticket[0] == start:
# #                 temp.append(ticket)
# #             else:
# #                 temp2.append(ticket)
# #
# #         if len(temp) != 0:
# #             temp.sort()
# #             temp_list = temp.pop(0)
# #             candidate.append(temp_list[1])
# #
# #         while temp:
# #             tickets.append(temp.pop())
# #
# #         while temp2:
# #             tickets.append(temp2.pop())
# #
# #     return answer
from _collections import defaultdict

def solution(tickets):

    STRART = 'ICN'
    dest = defaultdict(list)

    for ticket in tickets:
        dest[ticket[0]].append(ticket[1])

    for element in dest.keys():
        dest[element].sort()

    stack = []
    res = []

    def Search(start):
        stack = []
        stack.append(start)
        if len(dest[start]) == 0:
            top = stack.pop()
            res.append(top)
            return
        for element in dest[start][:]:
            if element not in dest[start]:
                continue
            dest[start].remove(element)
            Search(element)
        while stack:
            res.append(stack.pop())

    Search(STRART)
    res.reverse()

    return res

if __name__=="__main__":
    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    print(solution(tickets1))
    print(solution(tickets2))
