from collections import defaultdict


def solution(info, query):
    answer = []

    tree = defaultdict(list)
    for i in ["cpp", "java", "python", "-"]:
        tree[i] = defaultdict(list)
        for j in ["backend", "frontend", "-"]:
            tree[i][j] = defaultdict(list)
            for k in ["junior", "senior", "-"]:
                tree[i][j][k] = defaultdict(list)
                for z in ["chicken", "pizza", "-"]:
                    tree[i][j][k][z] = []

    for element in info:
        lang, job, exp, food, point = element.split()

        for i in [lang, "-"]:
            for j in [job, "-"]:
                for k in [exp, "-"]:
                    for z in [food, "-"]:
                        tree[i][j][k][z].append(int(point))

    for i in ["cpp", "java", "python", "-"]:
        for j in ["backend", "frontend", "-"]:
            for k in ["junior", "senior", "-"]:
                for z in ["chicken", "pizza", "-"]:
                    tree[i][j][k][z].sort()

    for qu in query:
        qu_list = qu.split(" ")
        qu_list.remove("and")
        qu_list.remove("and")
        qu_list.remove("and")

        lang, job, exp, food, point = qu_list
        candidate = tree[lang][job][exp][food]
        point = int(point)

        if len(candidate) > 0:
            start, end = 0, len(candidate)
            while end > start:
                mid = (start + end) // 2
                if candidate[mid] >= point:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(candidate) - start)
        else:
            answer.append(0)
    return answer

if __name__=="__main__":
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
                   ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]),
                    [1, 1, 1, 1, 2, 4])