# 使用pygame完成gui交互，是最终版
import pygame as pg
import os

class GameObject:
    def __init__(self, image, pos):
        self.image = image
        self.pos = image.get_rect(center= pos)

def load_image(name):
    path = os.path.join(main_dir, "data", name)
    return pg.image.load(path).convert_alpha()

def main(objects,board):
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    black = load_image("storn_black.png")
    white = load_image("storn_white.png")
    background = load_image("bg.png")

    # 窗体的标题
    pg.display.set_caption("五子棋")
    font = pg.font.Font('font/12345.TTF', 20)
    flag = 1
    going = True
    while going:
        if flag % 2 == 0:
            if pg.font:
                text = font.render("白棋回合", True, (255, 255, 255))  
        else:
            if pg.font:
                text = font.render("黑棋回合", True, (0, 0, 0))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=2)
        screen.blit(background, (0, 0))
        screen.blit(text, textpos)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if pos[0] > 587:
                    x = 14
                elif pos[0] < 27:
                    x = 0
                else:
                    x = round((pos[0] - 27)/40)
                if pos[1] > 587:
                    y = 14
                elif pos[1] < 27:
                    y = 0
                else:
                    y = round((pos[1] - 27)/40)
                if flag % 2 == 0:
                    if set_chess(board,x,y,'O'):
                        objects.append(GameObject(white,(27+x*40, 27+y*40)))
                        flag = 1
                    else:
                        hint_text = font.render("该位置已有棋子", True, (255, 255, 255))
                        hint_textpos = hint_text.get_rect(centerx=background.get_width() / 2, y=200)
                        # for o in objects:
                        #     screen.blit(o.image, o.pos)
                        screen.blit(hint_text, hint_textpos)
                        pg.display.update()
                        # pg.time.delay(300)
                else:
                    if set_chess(board,x,y,'X'):
                        objects.append(GameObject(black,(27+x*40, 27+y*40)))
                        flag = 0
                    else:
                        hint_text = font.render("该位置已有棋子", True, (255, 255, 255))
                        hint_textpos = hint_text.get_rect(centerx=background.get_width() / 2, y=200)
                        for o in objects:
                            screen.blit(o.image, o.pos)
                        screen.blit(hint_text, hint_textpos)
                        pg.display.update()
                        pg.time.delay(300)
        for o in objects:
            screen.blit(o.image, o.pos)
        if 0 in check_win_all(board):
            win_text = font.render("白棋获胜，游戏5秒后重新开始", True, (255, 255, 255))
            win_textpos = win_text.get_rect(centerx=background.get_width() / 2, y=200)
            screen.blit(win_text, win_textpos)
            pg.display.update()
            pg.time.delay(5000)
            board = [[' ']*15 for line in range(15)]
            objects = []
            flag = 1
        elif 1 in check_win_all(board):
            win_text = font.render("黑棋获胜，游戏5秒后重新开始", True, (0, 0, 0))
            win_textpos = win_text.get_rect(centerx=background.get_width() / 2, y=200)
            screen.blit(win_text, win_textpos)
            pg.display.update()
            pg.time.delay(5000)
            board = [[' ']*15 for line in range(15)]
            objects = []
            flag = 1
        clock.tick(60)
        pg.display.update()

def set_chess(board,x,y,color):
    if board[x][y] != ' ':
        print('该位置已有棋子')
        return False
    else:
        board[x][y] = color
        return True

def check_win(board):
    for list_str in board:
        if ''.join(list_str).find('O'*5) != -1:
            print('白棋获胜')
            return 0
        elif ''.join(list_str).find('X'*5) != -1:
            print('黑棋获胜')
            return 1
    else:
        return -1    

def check_win_all(board):
    board_c = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_c[x+y].append(board[x][y])
    board_d =  [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_d[x-y].append(board[x][y])
    return [check_win(board) , check_win([list(l) for l in zip(*board)]) , check_win(board_c) , check_win(board_d)]

if __name__ == "__main__":
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    WIDTH = 615
    HEIGHT = 615
    SPRITE_WIDTH = 36
    SPRITE_HEIGHT = 36
    board = [[' ']*15 for line in range(15)]
    objects = []
    main(objects,board)
    pg.quit()