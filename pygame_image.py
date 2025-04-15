import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#背景画像を読みだして描画
    koukaton_img = pg.image.load("fig/3.png")#工科とんの画像を読み込む。練習1
    koukaton_img = pg.transform.flip(koukaton_img, True, False) #練習2 こうかとんの左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = tmr #練習6
        screen.blit(bg_img, [-x, 0]) #画面サーフェスに座標ヨコ-x(変数),タテ0で画像を張り付けてね
        screen.blit(bg_img, [-x+1600, 0]) #練習7
        screen.blit(koukaton_img, [300, 200])  #練習4
        pg.display.update()
        tmr += 1        #タイマー変数
        clock.tick(200)  #FPSの指定 練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()