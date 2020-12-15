def solution(position):
    answer = 0
    col = ord(position[0]) - int(ord('a')) + 1
    row = int(position[1])
    dx = [1,-1,1,-1,2,-2,2,-2]
    dy = [2,2,-2,-2,1,1,-1,-1]

    for i in range(len(dx)):
        next_col = col + dx[i]
        next_row = row + dy[i]
        if next_row >= 1 and next_row <=8 and next_col <=8 and next_col >=1 :
            answer += 1

    return answer

if __name__=="__main__":
    position = 'a1'
    print(solution(position))