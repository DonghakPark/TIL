def solution(user_id, banned_id):
    answer = 1
    for ban in (banned_id):
        for i in range(1, len(banned_id)):
            if ban == banned_id[i]:
                banned_id.pop(i)
    sub = [0] * len(banned_id)
    k = 0

    for user in user_id:
        k = 0
        for ban in banned_id:
            if len(ban) == len(user):
                ban2 = ban.replace("*","")
                count = 0
                for element in range(len(ban2)):
                    if ban2[element] in user:
                        count += 1
                if count == len(ban2):
                    sub[k] += 1
            k += 1

    for i in sub:
        answer = answer * i
    return answer

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    result = solution(user_id, banned_id)
    print(result)
