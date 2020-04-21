board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    L = len(board)

    # stack
    stack = []

    # 위치 저장
    position = [-1] * L
    for y in range(L - 1, -1, -1):
        for x in range(L):
            if board[y][x] != 0:
                position[x] = y

    for i in range(L):
        if position[i] == -1:
            position[i] = L + 1

    for x in moves:


        if len(stack) == 0:
            if position[x-1] < L:
                stack.append(board[position[x-1]][x-1])
                position[x-1] += 1
        else:
            if position[x-1] < L:
                if stack[-1] == board[position[x-1]][x-1]:
                    stack.pop()
                    position[x-1] += 1
                    answer += 2

                else:
                    stack.append(board[position[x-1]][x-1])
                    position[x-1] += 1

    return answer

print(solution(board, moves))