#
# visit = [False] * len(words)
#
# stack = list()
#
# for element in range(len(words)):
#
#     if visit[element] == False:
#         stack.append(words[element])
#         visit[element] = True
#
#     while stack:
#
#         temp = stack.pop()
#
#         for element2 in range(len(words)):
#
#             count = 0
#             for a,b in zip(begin, words[element2]):
#                 if a == b:
#                     count += 1
#
#             if count == len(target)-1:
#                 stack.append(words[element2])
#                 begin = words[element2]
#                 visit[element2] = True
#                 answer += 1
#
#         if begin == target:
#             break
#
# answer = 0
#
# def bfs(begin, target, words, visited):
#     global answer
#     stacks = [begin]
#
#     while stacks:
#         stack = stacks.pop()
#
#         if stack == target:
#             return answer
#
#         for w in range(0,len(words)):
#             if len([i for i in range(0,len(words[w])) if words[w][i]!=stack[i]]) == 1:
#
#                 if visited[w] != 0:
#                     continue
#                 visited[w] = 1
#                 stacks.append(words[w])
#         answer += 1
#
# def solution(begin, target, words):
#
#     global answer
#
#     if target not in words:
#         return 0
#     visited = [0 for i in words]
#
#     bfs(begin, target, words, visited)
#
#     return answer

answer = 0
def solution(begin, target, words):

    dfs(begin, target, 0, words)
    return answer

def change(fr, to):
    for i in range(len(fr)):
        if fr[:i]+fr[i+1:] == to[:i]+to[i+1:]:
            return True
    return False

def dfs(begin, target, d, words):
    global answer

    if begin == target:
        answer = d
        return
    else:
        if len(words) == 0:
            return
        for w in range(len(words)):
            if change(begin, words[w]):
                word = words[:w]+ words[w+1:]
                dfs(words[w], target, d+1, word)

if __name__=="__main__":
    begin = 'hit'
    target = 'cog'
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(begin, target, words))
