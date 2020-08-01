def solution(board):
    visit = [[ False for i in range(5)] for j in range(5)]
    revisit = False

    col, row = 0,0
    answer = 0

    while True:

        #0,0일때
        if col == 0 and row == 0:

        #5,5 일때
        elif col == 5 and row == 5:

        else:

def compare(col,row,board):



if __name__ == "__main__":
    board = [["A","B","T","T","T"],["T","C","D","E","T"],["T","T","T","F","T"],
             ["B","A","H","G","F"],["C","D","E","F","G"]]

    print(solution(board))