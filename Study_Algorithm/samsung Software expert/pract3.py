def solution(moves):
    answer = 0
    count_arr = [moves.count("U"), moves.count("R"),moves.count("D"),moves.count("L")]
    count_arr.sort()
    answer = count_arr[0]
    return answer

if __name__=="__main__":
    moves = ["U","R","D","L","U","R","D","L"]
    print(solution(moves))