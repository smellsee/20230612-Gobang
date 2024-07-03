# 用pygame写小游戏的框架

# 导入pygame模块
import pygame as pg

# 模块初始化
pg.init()
# 基础设置：游戏窗口，帧率
WIDTH = 615
HEIGHT = 615
screen = pg.display.set_mode((WIDTH, HEIGHT)) # 游戏窗口
clock = pg.time.Clock() # 时钟帧率
objects = [] # 新创建的元素，全都放到这个列表里
# 导入素材
background = pg.image.load("data/bg.png").convert_alpha()
black = pg.image.load("data/storn_black.png").convert_alpha()
white = pg.image.load("data/storn_white.png").convert_alpha()
# 设置窗口标题
pg.display.set_caption("五子棋")

# 游戏主循环
going = True
while going:
    # 把背景图“打印”到窗口上
    screen.blit(background, (0, 0))
    # 根据玩家操作，执行对应指令
    for event in pg.event.get():
        # 如果关闭窗口，则主循环结束
        if event.type == pg.QUIT: 
            going = False
        # 如果点击键盘esc键，则主循环结束
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            going = False
        # 如果点击鼠标，则执行某个操作
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos() # 获取鼠标点击位置的坐标
            print(pos)
            objects.append([black,(pos[0]-18,pos[1]-18)])
    # 把objects列表里的所有对象都打印到窗口
    for o in objects:
        screen.blit(o[0], o[1])
    # 帧率设置为每秒60帧
    clock.tick(60)
    # 对游戏窗口进行刷新操作（如果不update，窗口是黑的。。。）
    pg.display.update()
# 如果循环结束，则关闭进程
pg.quit()