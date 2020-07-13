def solution(board, moves):
    answer = 0
    arr = [0,0]
    le = len(board[0])
    for m in moves:
        for i in range(le):
            try:
                if board[i][m-1] != 0:
                    arr.insert(0, board[i][m-1])
                    board[i].pop(m-1)
                    board[i].insert(m-1,0)
                    if arr[0] == arr[1]:
                        arr.pop(0)
                        arr.pop(0)
                        answer += 2
                    break
            except:
                continue

    return answer


if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    result = solution(board, moves)
    print(result)