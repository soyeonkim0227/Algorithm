def solution(board, moves):
    stack = []
    cnt = 0
    for d in moves: 
        for i in range(len(board)):
            if board[i][d-1] != 0:
                doll = board[i][d-1]
                board[i][d-1] = 0
                if stack and stack[-1] == doll:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(doll)
                break
    return cnt