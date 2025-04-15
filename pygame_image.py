import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#背景画像を読みだして描画
    bg_fliped_img = pg.transform.flip(bg_img, True, False)#練習8
    koukaton_img = pg.image.load("fig/3.png")#工科とんの画像を読み込む。練習1
    koukaton_img = pg.transform.flip(koukaton_img, True, False) #練習2 こうかとんの左右反転
    koukaton_rct = koukaton_img.get_rect() #練習10-1こうかとん座標抽出
    koukaton_rct.center = (300,200) #練習10-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()   #練習10-3
        if key_lst[pg.K_UP]:
            koukaton_rct.move_ip((0, -1))#練習10-4
        if key_lst[pg.K_DOWN]:
            koukaton_rct.move_ip((0, 1))#練習10-4
        if key_lst[pg.K_RIGHT]:
            koukaton_rct.move_ip((1, 0))#練習10-4
        if key_lst[pg.K_LEFT]:
            koukaton_rct.move_ip((-1, 0))#練習10-4


        x = tmr % 3200 #練習6,9 X座標はtmrを3200で割ったあまりになる。
        screen.blit(bg_img, [-x, 0]) #画面サーフェスに座標ヨコ-x(変数),タテ0で画像を張り付けてね
        screen.blit(bg_fliped_img, [-x+1600, 0]) #練習7
        screen.blit(bg_img, [-x+3200,0])#練習9
        screen.blit(koukaton_img,koukaton_rct) #練習4練習10-5
        pg.display.update()
        tmr += 1        #タイマー変数
        clock.tick(200)  #FPSの指定 練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()