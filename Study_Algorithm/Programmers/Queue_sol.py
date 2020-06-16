def solution(skill, skill_trees):
    answer =0
    skill_arr = list(skill)

    for element in skill_trees:
        Queue = []
        aa = True
        for i in element:
            if i in skill_arr:
                Queue.append(skill_arr.index(i))
        for j in range(0,len(Queue)):
            check = Queue.pop(0)
            if check != j:
                aa = False
        if aa ==True:
            answer = answer +1

    return answer

if __name__=="__main__":
    skill = 'CBD'
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill,skill_trees))