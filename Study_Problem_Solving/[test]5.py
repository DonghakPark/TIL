def solution(list_arr, clockwise):
    answer = []
    len_arr = len(list_arr)

    now_arr = [[False] * ((2*(len_arr -1)) + 1) for _ in range(len_arr)]


    first_pos = ((2 * (len_arr - 1)) // 2) -1
    word_len = 1
    now_index = 0
    while list_arr:
        now_word = list_arr.pop(0)

        now_word = list(now_word)

        for i in range(first_pos, first_pos + word_len):
            now_arr[now_index][i] = now_word.pop(0)

        word_len += 2
        now_index += 1

    for element in now_arr:
        print(*element)

    return answer

if __name__=="__main__":
    print(solution(["1","234","56789"], True),["5","762","98431"])
    print(solution(["A", "MAN", "DRINK", "WATER11"], False), ["1", "K1R", "NNIET", "AAMRDAW"])
