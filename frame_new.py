def set_chess(x,y,color):
    if board[x][y] != ' ':
        print('该位置已有棋子')
        return False
    else:
        board[x][y] = color
        for i in board:
            print(i)
        return True

def check_win(board):
    for line in board:
        if ''.join(line).find('O'*5) != -1:
            print('白棋获胜')
            return 0
        elif ''.join(line).find('X'*5) != -1:
            print('黑棋获胜')
            return 1
    else:
        return -1     

def check_win_all(board):
    board_c = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_c[x-y].append(board[x][y])
    board_d =  [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_d[x+y].append(board[x][y])
    return [check_win(board), check_win([list(l) for l in zip(*board)]), check_win(board_c), check_win(board_d)]          

if __name__ == '__main__':
    board = [[' ']*15 for line in range(15)]
    for i in board:
        print(i)
    flag = 0
    going = True
    while going:
        if flag == 0:
            print('黑棋回合')
            x = int(input('请输入棋子横坐标0-14：'))
            y = int(input('请输入棋子纵坐标0-14：'))
            set_chess(x,y,'X')
            flag = 1
            if 0 or 1 in check_win_all(board):
                going = False
        else:
            print('白棋回合')
            x = int(input('请输入棋子横坐标0-14：'))
            y = int(input('请输入棋子纵坐标0-14：'))
            set_chess(x,y,'O')
            flag = 0
            if 0 or 1 in check_win_all(board):
                going = False