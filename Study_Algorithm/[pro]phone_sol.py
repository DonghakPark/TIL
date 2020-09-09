def solution(phone_book):
    answer = True

    for element in range(0,len(phone_book)):
        len_m = len(phone_book[element])

        for element2 in range(element+1, len(phone_book)):
            len_m2 = len(phone_book[element2])
            if phone_book[element] == phone_book[element2][:len_m] or phone_book[element][:len_m2] == phone_book[element2]:
                answer = False
            else:
                continue

    return answer

if __name__=="__main__":
    phone_book = ["119", "97674223", "1195524421"]
    phone_book2 = ["123", "456", "789"]
    phone_book3 = ["12", "123", "1235", "567", "88"]
    print(solution(phone_book))
    print(solution(phone_book2))
    print(solution(phone_book3))