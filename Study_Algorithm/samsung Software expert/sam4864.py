T = int(input())
for test_case in range(1,T+1):
    str1 = list(input())
    str2 = list(input())
    arr = ""
    answer = 0
    for j in range(len(str2)-len(str1)+1):
        if str1[0] == str2[j]:
            arr = str2[j:j+len(str1)]
            if  arr == str1:
                answer = 1
            else:
                continue
    print("#%d %d" %(test_case, answer))
