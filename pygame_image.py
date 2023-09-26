import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    bird_img = pg.image.load("ex01/fig/3.png")
    bird_img = pg.transform.flip(bird_img,True,False)
    bird_img2 = pg.transform.rotozoom(bird_img,5,1.0)
    bird_imgs = [bird_img,bird_img2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200
        if tmr%100 <= 50:
            num = 0
        else:
            num = 1
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bird_imgs[num],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()