# 五子棋棋盘：一个15*15的棋盘
# python：用一个15*15的二维列表进行表示，即列表包含15个元素，每个元素均是列表且包含15个元素
board = [[' ']*15 for line in range(15)]
for line in board:
    print(line)

# 落子：黑棋白棋轮流落子，只能在把棋子落在两条线的交点上，已落子的地方不能再重复落子；
# python：
# 用循环+条件判断实现轮流落子
# 落子的过程，其实就是对二维列表的某个元素进行赋值操作
# 通过if条件判断，避免在重复落子

def set_chess(x,y,color):
    # 如果指定位置不为空（即有棋子），则提示“已有棋子”
    if board[x][y] != ' ':
        print('该位置已有棋子')
        return False
    # 如果指定位置为空，则进行赋值操作（落子）
    else:
        board[x][y] = color
        for i in board:
            print(i)
        return True

# 用X代表黑棋，O代表白棋
flag = 0
going = True
while going:
    if flag == 0:
        print('黑棋回合')
        x = int(input('请输入棋子横坐标0-14：'))
        y = int(input('请输入棋子纵坐标0-14：'))
        set_chess(x,y,'X')
        flag = 1
    else:
        print('白棋回合')
        x = int(input('请输入棋子横坐标0-14：'))
        y = int(input('请输入棋子纵坐标0-14：'))
        set_chess(x,y,'O')
        flag = 0


# 胜利条件：横、竖、正斜、反斜四个方向相同颜色五子连珠的一方，获胜；
# python：
# 横方向，检查board的每一行，查看是否有5个相同元素连在一起；
# 竖方向，检查board的每一列，查看是否有5个相同元素连在一起；
# 正斜、反斜方向，对board的元素进行重新分组，查看是否有5个相同元素连在一起；

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

board_b = [list(l) for l in zip(*board)]
board_c = [[] for line in range(29)]
for x in range(15):
    for y in range(15):
        board_c[x-y].append(board[x][y])
board_d =  [[] for line in range(29)]
for x in range(15):
    for y in range(15):
        board_d[x+y].append(board[x][y])

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