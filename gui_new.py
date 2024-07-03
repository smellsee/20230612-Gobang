import pygame as pg
if __name__ == '__main__':
    pg.init()
    WIDTH = 615
    HEIGHT = 615
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    black = pg.image.load("data/storn_black.png").convert_alpha()
    white = pg.image.load("data/storn_white.png").convert_alpha()
    background = pg.image.load("data/bg.png").convert_alpha()
    objects = []
    pg.display.set_caption("五子棋")
    going = True
    while going:
        screen.blit(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                print(pos)
                objects.append([black,(pos[0]-18,pos[1]-18)])
        for o in objects:
            screen.blit(o[0], o[1])        
        clock.tick(60)
        pg.display.update()
    pg.quit()