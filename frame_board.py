board = [[] for i in range(15)]

for i in range(15):
    for j in range(15):
        board[i].append((i,j))

# for line in board:
#     print(line)

board_b = [list(l) for l in zip(*board)]
# for line in board_b:
#     print(line)

board_c = [[] for line in range(29)]
for x in range(15):
    for y in range(15):
        board_c[x-y].append(board[x][y])
for line in board_c:
    print(line)

board_d =  [[] for line in range(29)]
for x in range(15):
    for y in range(15):
        board_d[x+y].append(board[x][y])
for line in board_d:
    print(line)