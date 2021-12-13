import sys

def solve(nums,boards):
    def play(board,num):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == num:
                    board[i][j] = -1
        for i in range(len(board)):
            cnt = 0
            for j in range(len(board[0])):
                if board[i][j] == -1:
                    cnt += 1
            if cnt == len(board[0]):
                return True
        for i in range(len(board[0])):
            cnt = 0
            for j in range(len(board)):
                if board[j][i] == -1:
                    cnt += 1
            if cnt == len(board):
                return True
        return False

    def score(board,num):
        cur = 0
        for row in board:
            for x in row:
                if x != -1:
                    cur += x
        return cur * num

    for num in nums:
        for board in boards:
            if play(board,num):
                return score(board,num)

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    nums = list(map(int,input().split(',')))
    boards = []
    board = []
    for line in sys.stdin:
        if line == "\n":
            if len(board) > 0:
                boards.append(board)
            board = []
        else:
            board.append(list(map(int,line.split())))
    boards.append(board)
    print(solve(nums,boards))