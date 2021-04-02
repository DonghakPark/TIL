def check_possible(first, second, tree):
    second_index = tree.index(second)

    if first in tree[:second_index + 1]:
        return True
    else:
        return False


def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        flag = True
        for i in range(1, len(skill)):
            if skill[i] in tree:
                flag = check_possible(skill[i - 1], skill[i], tree)
            if flag is False:
                break
        if flag:
            answer += 1
        else:
            continue

    return answer

if __name__=="__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]), 2)