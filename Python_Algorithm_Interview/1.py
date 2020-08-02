def isPalindrome(s: str) -> bool:

    answer = False

    str1 = []
    str2 = []
    s = s.lower()

    for s_s in s:
        if s_s >='a' and s_s <='z':
            str1.append(s_s)
            str2.insert(0, s_s)
        elif s_s >= '0' and s_s <= '9':
            str1.append(s_s)
            str2.insert(0, s_s)
    if str1 == str2:
        answer = True

    return answer

if __name__=="__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))
