import pygame
import os
import time
pygame.font.init()
pygame.font.init()
pygame.mixer.init()
WIDTH = 960
HEIGHT=810

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pac man")

purple=(240,0,255)

background= pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'base3.png')), (WIDTH, HEIGHT))
back= pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'back.jpg')), (WIDTH, HEIGHT))
scorefont=pygame.font.SysFont('comicsans', 50)


yellow=(255,200,0)



p_image = pygame.image.load(
    os.path.join('Assets', 'pac2.png'))
p_image2 = pygame.image.load(
    os.path.join('Assets', 'pac.png'))
p_image3 = pygame.image.load(
    os.path.join('Assets', 'pac3.png'))
pac=pygame.transform.scale(
    p_image, (15,15))

ghostimage=pygame.image.load(os.path.join('Assets', 'ghost1.png'))
ghost_=pygame.transform.scale(
    ghostimage, (40,45))



speed=8
pspeed=4
white=(255,255,255)

FPS=30
def newgame(score):
        WIN.blit(back, (0, 0))
        score_text2 = scorefont.render(
            "Try again", 1, white)
        WIN.blit(score_text2, (90, 80))
        score_text2 = scorefont.render(
            "Press r to restart", 1, white)
        WIN.blit(score_text2, (30, 115))
        score_text = scorefont.render(
            "Score: " + str(score), 1, white)
        WIN.blit(score_text, (5, 10))
        pygame.display.update()
def drawwindow(pacman,pac,ghost,ghost1,count1,ghost2,count2,count3,ghost3,food1_1,food1_2,food1_3,food1_4,
        food1_5,food1_6,food1_10,food1_11,food1_12,food1_13,food1_14,
        food1_15,food2_1,food2_4,food2_6,food2_8,food2_10,food2_12,food2_15,food3_1,food3_2,food3_3,food3_4,
        food3_6,food3_8,food3_10,food3_12,food3_13,food3_14,
        food3_15,food4_1,food4_5,food4_6,food4_7,food4_8,food4_9,food4_10,food4_11,food4_15,food5_1,food5_2,
         food5_3,food5_4,food5_5,food5_11,food5_12,food5_13,food5_14,food5_15,food6_1,food6_3,food6_5,food6_11,
         food6_13,food6_14,food7_1,food7_3,food7_5,food7_11,food7_13,food8_1,food8_3,food8_5,food8_11,food8_13,
         food8_14,food9_1,food9_2,food9_3,food9_4,food9_5,food9_6,food9_7,food9_8,food9_9,food9_10,food9_11,
         food9_12,food9_13,food9_14,food9_15,food10_1,food10_3,food10_4, food10_5,  food10_6,food10_11,
         food10_12,food10_13,food10_15,food11_1,food11_5,food11_6,food11_11,food11_15,food12_1,food12_2,
         food12_3,food12_4,food12_5,food12_6,food12_11,food12_12,food12_13,food12_14,food12_15,score):
    WIN.blit(background,(0,0))
    score_text = scorefont.render(
        "Score: " + str(score), 1, yellow)
    WIN.blit(score_text, (415, 380))

    WIN.blit(pac, (pacman.x, pacman.y))
    if food1_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,50,15,15))
    if food1_2== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(110,50,15,15))
    if food1_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,50,15,15))
    if food1_4== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(230,50,15,15))
    if food1_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,50,15,15))
    if food1_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,50,15,15))

    if food1_10== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(590,50,15,15))
    if food1_11== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650,50,15,15))
    if food1_12== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(710,50,15,15))
    if food1_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,50,15,15))
    if food1_14== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(830,50,15,15))
    if food1_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,50,15,15))
    #2 row
    if food2_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,110,15,15))
    pygame.display.update()
    if food2_4== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(230,110,15,15))
    if food2_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,110,15,15))
    if food2_8== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(470,110,15,15))
    if food2_10== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(590,110,15,15))
    if food2_12== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(710,110,15,15))
    if food2_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,110,15,15))
    #row3
    if food3_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,170,15,15))
    if food3_2== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(110,170,15,15))
    if food3_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,170,15,15))
    if food3_4== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(230,170,15,15))
    if food3_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,170,15,15))
    if food3_8== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(470,170,15,15))
    if food3_10== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(590,170,15,15))
    if food3_12== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(710,170,15,15))
    if food3_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,170,15,15))
    if food3_14== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(830,170,15,15))
    if food3_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,170,15,15))
    #row4
    if food4_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,230,15,15))
    if food4_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,230,15,15))
    if food4_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,230,15,15))
    if food4_7== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(410,230,15,15))
    if food4_8== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(470,230,15,15))
    if food4_9== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(530,230,15,15))
    if food4_10 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(590,230, 15, 15))
    if food4_11 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650, 230, 15, 15))
    if food4_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,230,15,15))
    #row5
    if food5_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,290,15,15))
    if food5_2== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(110,290,15,15))
    if food5_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,290,15,15))
    if food5_4== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(230,290,15,15))
    if food5_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,290,15,15))
    if food5_11== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650,290,15,15))
    if food5_12== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(710,290,15,15))
    if food5_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,290,15,15))
    if food5_14== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(830,290,15,15))
    if food5_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,290,15,15))
    #row6
    if food6_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,350,15,15))
    if food6_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,350,15,15))
    if food6_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,350,15,15))
    if food6_11== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650,350,15,15))
    if food6_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,350,15,15))
    if food6_14== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(830,350,15,15))
    #row7
    if food7_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,410,15,15))
    if food7_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,410,15,15))
    if food7_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,410,15,15))
    if food7_11== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650,410,15,15))
    if food7_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,410,15,15))
    #row8
    if food8_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,470,15,15))
    if food8_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,470,15,15))
    if food8_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,470,15,15))
    if food8_11== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650,470,15,15))
    if food8_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,470,15,15))
    if food8_14== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(830,470,15,15))
    #row9
    if food9_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,530,15,15))
    if food9_2== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(110,530,15,15))
    if food9_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,530,15,15))
    if food9_4== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(230,530,15,15))
    if food9_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,530,15,15))
    if food9_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,530,15,15))
    if food9_7== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(410,530,15,15))
    if food9_8== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(470,530,15,15))
    if food9_9== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(530,530,15,15))
    if food9_10 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(590,530, 15, 15))
    if food9_11 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650, 530, 15, 15))
    if food9_12== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(710,530,15,15))
    if food9_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,530,15,15))
    if food9_14== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(830,530,15,15))
    if food9_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,530,15,15))
    #row10
    if food10_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,590,15,15))
    if food10_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,590,15,15))
    if food10_4== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(230,590,15,15))
    if food10_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,590,15,15))
    if food10_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,590,15,15))
    if food10_11 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650, 590, 15, 15))
    if food10_12== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(710,590,15,15))
    if food10_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,590,15,15))
    if food10_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,590,15,15))
    #row11
    if food11_1 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50, 650, 15, 15))
    if food11_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,650,15,15))
    if food11_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,650,15,15))
    if food11_11 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650, 650, 15, 15))
    if food11_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,650,15,15))
    #row12
    if food12_1== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(50,710,15,15))
    if food12_2== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(110,710,15,15))
    if food12_3== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(170,710,15,15))
    if food12_4== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(230,710,15,15))
    if food12_5== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(290,710,15,15))
    if food12_6== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(350,710,15,15))
    if food12_11 == True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(650, 710, 15, 15))
    if food12_12== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(710,710,15,15))
    if food12_13== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(770,710,15,15))
    if food12_14== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(830,710,15,15))
    if food12_15== True:
        pygame.draw.rect(WIN, yellow, pygame.Rect(890,710,15,15))
    WIN.blit(ghost_, (ghost.x, ghost.y))
    if count1 >=120:
        WIN.blit(ghost_, (ghost1.x, ghost1.y))
    if count2 >=200:
        WIN.blit(ghost_, (ghost2.x, ghost2.y))
    if count3 >=400:
        WIN.blit(ghost_, (ghost3.x, ghost3.y))

    pygame.display.update()



def mainloop():
    right = pygame.transform.scale(
        p_image, (40, 40))
    left = pygame.transform.rotate(pygame.transform.scale(
        p_image, (40, 40)), 180)
    down = pygame.transform.rotate(pygame.transform.scale(
        p_image, (40, 40)), 270)
    up = pygame.transform.rotate(pygame.transform.scale(
        p_image, (40, 40)), 90)
    pac = right
    pacman = pygame.Rect(460, 40, 15, 15)
    ghost=pygame.Rect(510,700,15,15)
    ghost1 = pygame.Rect(510, 700, 15, 15)
    ghost2 = pygame.Rect(510, 700, 15, 15)
    ghost3 = pygame.Rect(510, 700, 15, 15)
    frame=0
    clock = pygame.time.Clock()
    run = True
    ghost1run=True #ghost1
    ghost1run2 = False
    ghost1run3= 4
    gamerun=True

    count1=0
    count2=0
    count3=0
    ghost2run= False #ghost2
    ghost2run1 = False
    ghost2run2 = False
    ghost2run3= False
    run2=0 #zaciatok 3.ghosta
    run3=0 #ghost3
    run4=0 #ghost4
    score=0
    food1_1=True
    food1_2=True
    food1_3=True
    food1_4=True
    food1_5=True
    food1_6=True
    food1_10 = True
    food1_11= True
    food1_12= True
    food1_13= True
    food1_14= True
    food1_15= True
    food2_1 = True
    food2_4 = True
    food2_6 = True
    food2_8 = True
    food2_10 = True
    food2_12 = True
    food2_15 = True

    food3_1 = True
    food3_2 = True
    food3_3 = True
    food3_4 = True
    food3_6 = True
    food3_8 = True
    food3_10 = True
    food3_12 = True
    food3_13 = True
    food3_14 = True
    food3_15 = True
    food4_1= True
    food4_5= True
    food4_6= True
    food4_7= True
    food4_8= True
    food4_9= True
    food4_10= True
    food4_11= True
    food4_15= True
    food5_1= True
    food5_2= True
    food5_3= True
    food5_4= True
    food5_5= True
    food5_11= True
    food5_12= True
    food5_13= True
    food5_14= True
    food5_15= True
    food6_1= True
    food6_3= True
    food6_5= True
    food6_11= True
    food6_13= True
    food6_14= True
    food7_1= True
    food7_3= True
    food7_5= True
    food7_11= True
    food7_13= True
    food8_1= True
    food8_3= True
    food8_5= True
    food8_11= True
    food8_13= True
    food8_14= True
    food9_1=True
    food9_2=True
    food9_3=True
    food9_4=True
    food9_5=True
    food9_6=True
    food9_7=True
    food9_8=True
    food9_9=True
    food9_10=True
    food9_11=True
    food9_12=True
    food9_13=True
    food9_14=True
    food9_15=True
    food10_1=True
    food10_3=True
    food10_4=True
    food10_5=True
    food10_6=True
    food10_11=True
    food10_12=True
    food10_13=True
    food10_15=True
    food11_1=True
    food11_5=True
    food11_6=True
    food11_11=True
    food11_15=True
    food12_1=True
    food12_2=True
    food12_3=True
    food12_4=True
    food12_5=True
    food12_6=True
    food12_11=True
    food12_12=True
    food12_13=True
    food12_14=True
    food12_15=True
    count4=0

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_r]:
                mainloop()
        if count4<=399:
            count4+=1
        if gamerun==False:
            newgame(score)
        elif gamerun==True:
            if count4>=201:
                if keys_pressed[pygame.K_d]:
                    if pacman.x <= 885:
                        pacman.x += pspeed
                        pac = right
                        if pacman.x<=60 and pacman.x>=50 and pacman.y>=60 and pacman.y<= 150:
                            pacman.x-=pspeed
                        if pacman.y >= 180 and pacman.y <= 270 and pacman.x and pacman.x<=90 and pacman.x>=50:
                            pacman.x-=pspeed
                        if pacman.y >=300 and pacman.y<= 510 and pacman.x>=50 and pacman.x<=70:
                            pacman.x -= pspeed
                        if pacman.y >=530 and pacman.y<= 690 and pacman.x>=50 and pacman.x<=70:
                            pacman.x -= pspeed
                        if pacman.y >=60 and pacman.y<= 210 and pacman.x>=230 and pacman.x<=240:
                            pacman.x -= pspeed
                        if pacman.y >=300 and pacman.y<= 510 and pacman.x>=170 and pacman.x<=180:
                            pacman.x -= pspeed
                        if pacman.y >=30 and pacman.y<= 210 and pacman.x>=350 and pacman.x<=360:
                            pacman.x -=pspeed
                        if pacman.y >=240 and pacman.y<= 500 and pacman.x>=285 and pacman.x<=295:
                            pacman.x -= pspeed
                        if pacman.y >=30 and pacman.y<= 210 and pacman.x>=470 and pacman.x<=480:
                            pacman.x -= pspeed
                        if pacman.y >=540 and pacman.y<= 750 and pacman.x>=350 and pacman.x<=360:
                            pacman.x -= pspeed
                        if pacman.y >=60 and pacman.y<= 210 and pacman.x>=590 and pacman.x<=600:
                            pacman.x -= pspeed
                        if pacman.y >= 210 and pacman.y <= 270 and pacman.x >= 650 and pacman.x <= 660:
                                pacman.x -= pspeed
                        if pacman.y >= 60 and pacman.y <= 150 and pacman.x >= 710 and pacman.x <= 720:
                                pacman.x -= pspeed
                        if pacman.y >= 290 and pacman.y <= 510 and pacman.x >= 650 and pacman.x <= 660:
                                pacman.x -= pspeed
                        if pacman.y >= 290 and pacman.y <= 390 and pacman.x >= 830 and pacman.x <= 840:
                                pacman.x -= pspeed
                        if pacman.y >= 350 and pacman.y <= 450 and pacman.x >= 770 and pacman.x <= 780:
                                pacman.x -= pspeed
                        if pacman.y >= 440 and pacman.y <= 510 and pacman.x >= 830 and pacman.x <= 840:
                                pacman.x -= pspeed
                        if pacman.y >= 600 and pacman.y <= 690 and pacman.x >= 650 and pacman.x <= 660:
                                pacman.x -= pspeed
                        if pacman.y >= 530 and pacman.y <= 630 and pacman.x >= 770 and pacman.x <= 780:
                                pacman.x -= pspeed
                if keys_pressed[pygame.K_s]:
                    if pacman.y <= 710:
                        pacman.y += pspeed
                        pac = down

                        if pacman.x >= 60 and pacman.x <= 210 and pacman.y <= 90 and pacman.y >= 50:
                            pacman.y -= pspeed
                        if pacman.y > 170 and pacman.y <= 200 and pacman.x >= 60 and pacman.x <= 270:
                            pacman.y -= pspeed
                        if pacman.y >= 290 and pacman.y <= 305 and pacman.x >= 50 and pacman.x <= 150:
                            pacman.y -= pspeed
                        if pacman.y >= 530 and pacman.y <= 545 and pacman.x >= 60 and pacman.x <= 140:
                            pacman.y -= pspeed
                        if pacman.y >= 590 and pacman.y <= 605 and pacman.x >= 120 and pacman.x <= 260:
                            pacman.y -= pspeed
                        if pacman.y >= 50 and pacman.y <= 65 and pacman.x >= 230 and pacman.x <= 330:
                            pacman.y -= pspeed
                        if pacman.y >= 230 and pacman.y <= 240 and pacman.x >= 300 and pacman.x <= 630:
                            pacman.y -= pspeed
                        if pacman.y >= 290 and pacman.y <= 300 and pacman.x >= 180 and pacman.x <= 270:
                            pacman.y -= pspeed
                        if pacman.y >= 530 and pacman.y <= 540 and pacman.x >= 350 and pacman.x <= 630:
                            pacman.y -= pspeed
                        if pacman.y >= 50 and pacman.y <= 60 and pacman.x >= 590 and pacman.x <= 690:
                            pacman.y -= pspeed
                        if pacman.y >= 170 and pacman.y <= 180 and pacman.x >= 690 and pacman.x <= 870:
                            pacman.y -= pspeed
                        if pacman.y >= 50 and pacman.y <= 60 and pacman.x >= 720 and pacman.x <= 870:
                            pacman.y -= pspeed
                        if pacman.y >= 290 and pacman.y <= 300 and pacman.x >= 660 and pacman.x <= 750:
                            pacman.y -= pspeed
                        if pacman.y >= 290 and pacman.y <= 300 and pacman.x >= 830 and pacman.x <= 910:
                            pacman.y -= pspeed
                        if pacman.y >= 350 and pacman.y <= 360 and pacman.x >= 770 and pacman.x <= 850:
                            pacman.y -= pspeed
                        if pacman.y >= 530 and pacman.y <= 540 and pacman.x >= 770 and pacman.x <= 870:
                            pacman.y -= pspeed
                        if pacman.y >= 590 and pacman.y <= 600 and pacman.x >= 650 and pacman.x <= 810:
                            pacman.y -= pspeed
                if keys_pressed[pygame.K_w]:
                    if pacman.y >= 40:
                        pac = up
                        pacman.y -= pspeed
                        if pacman.x>=60 and pacman.x<=210 and pacman.y<=150 and pacman.y>=130:
                            pacman.y+=pspeed
                        if pacman.y>= 250 and pacman.y<=265 and pacman.x>=60 and pacman.x<= 270:
                            pacman.y+=pspeed
                        if pacman.y>= 505 and pacman.y<=510 and pacman.x>=60 and pacman.x<= 150:
                            pacman.y+=pspeed
                        if pacman.y>= 680 and pacman.y<=690 and pacman.x>=60 and pacman.x<= 270:
                            pacman.y+=pspeed
                        if pacman.y>= 200 and pacman.y<=210 and pacman.x>=260 and pacman.x<= 330:
                            pacman.y+=pspeed
                        if pacman.y>= 500 and pacman.y<=510 and pacman.x >= 300 and pacman.x <= 630:
                            pacman.y+=pspeed
                        if pacman.y>= 200 and pacman.y<=210 and pacman.x >= 350 and pacman.x <= 450:
                            pacman.y+=pspeed
                        if pacman.y >= 200 and pacman.y <= 210 and pacman.x >= 470 and pacman.x <= 570:
                            pacman.y+=pspeed
                        if pacman.y >= 500 and pacman.y <= 510 and pacman.x >= 170 and pacman.x <= 270:
                            pacman.y+=pspeed
                        if pacman.y >= 200 and pacman.y <= 210 and pacman.x >= 590 and pacman.x <= 690:
                            pacman.y+=pspeed
                        if pacman.y >= 260 and pacman.y <= 270 and pacman.x >= 650 and pacman.x <= 870:
                            pacman.y+=pspeed
                        if pacman.y >= 140 and pacman.y <= 150 and pacman.x >= 710 and pacman.x <= 870:
                            pacman.y+=pspeed
                        if pacman.y >= 500 and pacman.y <= 510 and pacman.x >= 660 and pacman.x <= 750:
                            pacman.y+=pspeed
                        if pacman.y >= 440 and pacman.y <= 450 and pacman.x >= 770 and pacman.x <= 850:
                            pacman.y+=pspeed
                        if pacman.y >= 500 and pacman.y <= 510 and pacman.x >= 830 and pacman.x <= 910:
                            pacman.y+=pspeed
                        if pacman.y >= 680 and pacman.y <= 690 and pacman.x >= 660 and pacman.x <= 870:
                            pacman.y+=pspeed
                if keys_pressed[pygame.K_a]:
                    if pacman.x >= 35:
                        pac = left
                        pacman.x -= pspeed
                        if pacman.x>=200 and pacman.x<=210 and pacman.y>=60 and pacman.y<= 150:
                            pacman.x += pspeed
                        if pacman.x>= 250 and pacman.x<=270 and pacman.y>= 190 and pacman.y<=270:
                            pacman.x+=pspeed
                        if pacman.x>= 140 and pacman.x<=150 and pacman.y >=300 and pacman.y<= 510:
                            pacman.x+=pspeed
                        if pacman.y >=530 and pacman.y<= 690 and pacman.x>=130 and pacman.x<=150:
                            pacman.x += pspeed
                        if pacman.y >=590 and pacman.y<= 690 and pacman.x>=250 and pacman.x<=270:
                            pacman.x += pspeed
                        if pacman.y >=50 and pacman.y<= 210 and pacman.x>=320 and pacman.x<=330:
                            pacman.x += pspeed
                        if pacman.y >=300 and pacman.y<= 510 and pacman.x>=260 and pacman.x<=270:
                            pacman.x += pspeed
                        if pacman.y >=30 and pacman.y<= 200 and pacman.x>=440 and pacman.x<=450:
                            pacman.x += pspeed
                        if pacman.y >=240 and pacman.y<= 510 and pacman.x>=620 and pacman.x<=630:
                            pacman.x += pspeed
                        if pacman.y >=30 and pacman.y<= 210 and pacman.x>=560 and pacman.x<=570:
                            pacman.x += pspeed
                        if pacman.y >530 and pacman.y<= 800 and pacman.x>=620 and pacman.x<=630:
                            pacman.x += pspeed
                        if pacman.y >50 and pacman.y<= 210 and pacman.x>=680 and pacman.x<=690:
                            pacman.x += pspeed
                        if pacman.y >180 and pacman.y<= 270 and pacman.x>=860 and pacman.x<=870:
                            pacman.x += pspeed
                        if pacman.y >60 and pacman.y<= 150 and pacman.x>=860 and pacman.x<=870:
                            pacman.x += pspeed
                        if pacman.y >290 and pacman.y<= 510 and pacman.x>=740 and pacman.x<=750:
                            pacman.x += pspeed
                        if pacman.y >530 and pacman.y<= 690 and pacman.x>=860 and pacman.x<=870:
                            pacman.x += pspeed


            if ghost.x<=90 and ghost.y < pacman.y and ghost1run2 == True and pacman.x <=70 and pacman.y>=0 and pacman.y<=750:
                ghost1run=False #ghost1
                ghost1run2 = False
                ghost1run3= 1
            elif ghost.x<=90 and ghost.y > pacman.y and ghost1run3 == 1 and pacman.x <=70 and pacman.y>=0 and pacman.y<=750:
                ghost1run=False #ghost1
                ghost1run2 = True
                ghost1run3= 4

            else:
                if ghost1run == True:
                    ghost.x-=speed
                    if ghost.x <=45:
                        ghost1run = False
                        ghost1run2 = True
                if ghost1run2 == True:
                    ghost.y-=speed
                    if ghost.y <= 45:
                        ghost1run2 = False
                        ghost1run3 = 5
                if ghost1run3 == 5:
                    ghost.x +=speed
                    if ghost.x >=350:
                        ghost1run3=0
                if ghost1run3 == 0:
                    ghost.x-=speed
                    if ghost.x <= 45:
                            ghost1run3 =1
                if ghost1run3 == 1:
                    ghost.y+=speed
                    if ghost.y >= 700:
                        ghost1run3 = 2
                if ghost1run3 ==2:
                    ghost.x +=speed
                    if ghost.x >=350:
                        ghost1run3=4
                        ghost1run2=False
                        ghost1run=True



            if count1<=120:
                count1+=1


            if count1>=120:
                if ghost1.x >= 280 and ghost1.x <= 570 and ghost1.y >= 600 and ghost1.y <= 750:
                    ghost1.x -= speed
                    if ghost1.x<=280:
                        ghost2run=True
                        count1+=1
                if ghost2run == True:
                    ghost1.y -=speed
                    if ghost1.y<=220:
                        ghost2run = False
                        ghost2run1 =True
                if ghost2run1 == True:
                    ghost1.x+=speed
                    if ghost1.x>=640:
                        ghost2run1=False
                        ghost2run2=True
                if ghost2run2== True:
                    ghost1.y +=speed
                    if ghost1.y>=515:
                        ghost2run2=False
                        ghost2run3=True
                if ghost2run3 == True:
                    ghost1.x -=speed
                    if ghost1.x<=280:
                        ghost2run = True
                        ghost2run1 = False
                        ghost2run2 = False
                        ghost2run3 = False


                if count2<=200:
                    count2+=1
                if count2 >= 200:
                    if ghost2.x >= 345 and ghost2.x <= 570 and ghost2.y >= 600 and ghost2.y <= 750:
                        ghost2.x -= speed
                        if ghost2.x <= 345:
                            run2=1
                    if run2 == 1:
                        ghost2.y -=speed
                        if ghost2.y<=520:
                            run2=2
                    if run2 == 2:
                        ghost2.x+=speed
                        if ghost2.x >= 640:
                            run2=3
                    if run2 == 3:
                        ghost2.y+=speed
                        if ghost2.y >= 695:
                            run2=0
                            run3=1
                    if run3 == 1:
                        ghost2.x+=speed
                        if ghost2.x>=880:
                            run3=2
                    if run3==2:
                        ghost2.y-=speed
                        if ghost2.y<= 515:
                            run3=3
                    if run3 == 3:
                        ghost2.x-=speed
                        if ghost2.x<=760:
                            run3=4
                    if run3 == 4:
                        ghost2.y-=speed
                        if ghost2.y <=275:
                            run3 = 5
                    if run3 == 5:
                        ghost2.x +=speed
                        if ghost2.x >=880:
                            run3=6
                    if run3 == 6:
                        ghost2.y -= speed
                        if ghost2.y <= 40:
                            run3 =7
                    if run3 == 7:
                        ghost2.x-=speed
                        if ghost2.x<=700:
                            run3=8
                    if run3==8:
                        ghost2.y+=speed
                        if ghost2.y>= 155:
                            run3=9
                    if run3 == 9:
                        ghost2.x+=speed
                        if ghost2.x>=880:
                            run3 = 10
                    if run3 == 10:
                        ghost2.y+=speed
                        if ghost2.y >= 275:
                            run3 =11
                    if run3 ==11:
                        ghost2.x -= speed
                        if ghost2.x <= 760:
                            run3 = 12
                    if run3 ==12:
                        ghost2.y+=speed
                        if ghost2.y>= 575:
                            run3=13
                    if run3 == 13:
                        ghost2.x -= speed
                        if ghost2.x <= 700:
                            run3 =14
                    if run3 == 14:
                        ghost2.y+=speed
                        if ghost2.y>=575:
                            run3=15
                    if run3 == 15:
                        ghost2.x -= speed
                        if ghost2.x <=640:
                            run3=16
                    if run3 == 16:
                        ghost2.y +=speed
                        if ghost2.y>= 695:
                            run3=1

            if count3 <= 400:
                count3 += 1
            if count3 >= 400:
                if ghost3.x >= 280 and ghost3.x <= 570 and ghost3.y >= 600 and ghost3.y <= 750:
                    ghost3.x -= speed
                    if ghost3.x <= 280:
                        run4=1
                if run4 == 1:
                    ghost3.y -=speed
                    if ghost3.y<=580:
                        run4=2
                if run4 == 2:
                    ghost3.x-=speed
                    if ghost3.x <=160:
                        run4 = 3
                if run4 == 3:
                    ghost3.y-=speed
                    if ghost3.y<=270:
                        run4=4
                if run4 == 4:
                    ghost3.y +=speed
                    if ghost3.y>=580:
                        run4=5
                if run4 == 5:
                    ghost3.x+=speed
                    if ghost3.x >=220:
                        run4 =  6
                if run4 == 6:
                    ghost3.y -= speed
                    if ghost3.y<=520:
                        run4 = 7
                if run4 == 7:
                    ghost3.x-=speed
                    if ghost3.x<=160:
                        run4=3














        frame += 12
        if frame == 60:
            right = pygame.transform.scale(
                p_image3, (40, 40))
            left = pygame.transform.rotate(pygame.transform.scale(
                p_image3, (40, 40)), 180)
            down = pygame.transform.rotate(pygame.transform.scale(
                p_image3, (40, 40)), 270)
            up = pygame.transform.rotate(pygame.transform.scale(
                p_image3, (40, 40)), 90)
        if frame == 120:
            right = pygame.transform.scale(
                p_image2, (40, 40))
            left = pygame.transform.rotate(pygame.transform.scale(
                p_image2, (40, 40)), 180)
            down = pygame.transform.rotate(pygame.transform.scale(
                p_image2, (40, 40)), 270)
            up = pygame.transform.rotate(pygame.transform.scale(
                p_image2, (40, 40)), 90)
        if frame == 180:
            right = pygame.transform.scale(
                p_image, (40, 40))
            left = pygame.transform.rotate(pygame.transform.scale(
                p_image, (40, 40)), 180)
            down = pygame.transform.rotate(pygame.transform.scale(
                p_image, (40, 40)), 270)
            up = pygame.transform.rotate(pygame.transform.scale(
                p_image, (40, 40)), 90)
        if frame == 240:
            right = pygame.transform.scale(
                p_image3, (40, 40))
            left = pygame.transform.rotate(pygame.transform.scale(
                    p_image3, (40, 40)), 180)
            down = pygame.transform.rotate(pygame.transform.scale(
                p_image3, (40, 40)), 270)
            up = pygame.transform.rotate(pygame.transform.scale(
                p_image3, (40, 40)), 90)
        if frame == 300:
            right = pygame.transform.scale(
                p_image2, (40, 40))
            left = pygame.transform.rotate(pygame.transform.scale(
                p_image2, (40, 40)), 180)
            down = pygame.transform.rotate(pygame.transform.scale(
                p_image2, (40, 40)), 270)
            up = pygame.transform.rotate(pygame.transform.scale(
                p_image2, (40, 40)), 90)
        if frame == 360:
            right = pygame.transform.scale(
                p_image, (40, 40))
            left = pygame.transform.rotate(pygame.transform.scale(
                p_image, (40, 40)), 180)
            down = pygame.transform.rotate(pygame.transform.scale(
                p_image, (40, 40)), 270)
            up = pygame.transform.rotate(pygame.transform.scale(
                p_image, (40, 40)), 90)
            frame = 0

        if pacman.colliderect(ghost) or ghost.colliderect(pacman) or\
                pacman.colliderect(ghost1) or ghost1.colliderect(pacman) or \
                pacman.colliderect(ghost2) or ghost2.colliderect(pacman)or \
                pacman.colliderect(ghost3) or ghost3.colliderect(pacman):

            gamerun = False

        if score==106:

            gamerun = False
            newgame(score)

        if gamerun==True:
            drawwindow(pacman,pac,ghost,ghost1,count1,ghost2,count2,count3,ghost3,food1_1,food1_2,food1_3,food1_4,
            food1_5,food1_6,food1_10,food1_11,food1_12,food1_13,food1_14,
            food1_15,food2_1,food2_4,food2_6,food2_8,food2_10,food2_12,food2_15,food3_1,food3_2,food3_3,food3_4,
            food3_6,food3_8,food3_10,food3_12,food3_13,food3_14,food3_15,food4_1,food4_5,food4_6,food4_7,food4_8,
            food4_9,food4_10,food4_11,food4_15,food5_1,food5_2,food5_3,food5_4,food5_5,food5_11,food5_12,food5_13,
            food5_14,food5_15,food6_1,food6_3,food6_5,food6_11,food6_13,food6_14,food7_1,food7_3,food7_5,food7_11,
            food7_13,food8_1,food8_3,food8_5,food8_11,food8_13,food8_14,food9_1,food9_2,food9_3,food9_4,food9_5,food9_6,
            food9_7,food9_8,food9_9,food9_10,food9_11,food9_12,food9_13,food9_14,food9_15,food10_1,food10_3,food10_4,
            food10_5,  food10_6,food10_11,food10_12,food10_13,food10_15,food11_1,food11_5,food11_6,food11_11,food11_15,
            food12_1,food12_2,food12_3,food12_4,food12_5,food12_6,food12_11,food12_12,food12_13,food12_14,food12_15,score)

        #fucking food
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=30 and pacman.y<=60  and food1_1 == True:
            food1_1 = False
            score+=1
        if pacman.x >= 90 and pacman.x <= 120 and pacman.y >= 30 and pacman.y <= 60 and food1_2 == True:
            food1_2 = False
            score += 1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 30 and pacman.y <= 60 and food1_3 == True:
            food1_3 = False
            score += 1
        if pacman.x >= 210 and pacman.x <= 240 and pacman.y >= 30 and pacman.y <= 60 and food1_4 == True:
            food1_4 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 30 and pacman.y <= 60 and food1_5 == True:
            food1_5 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 30 and pacman.y <= 60 and food1_6 == True:
            food1_6 = False
            score += 1
        if pacman.x >= 570 and pacman.x <= 600 and pacman.y >= 30 and pacman.y <= 60 and food1_10 == True :
            food1_10 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 30 and pacman.y <= 60 and food1_11 == True:
            food1_11 = False
            score += 1
        if pacman.x >= 690 and pacman.x <= 720 and pacman.y >= 30 and pacman.y <= 60 and food1_12 == True:
            food1_12 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 30 and pacman.y <= 60 and food1_13 == True:
            food1_13 = False
            score += 1
        if pacman.x >= 810 and pacman.x <= 840 and pacman.y >= 30 and pacman.y <= 60 and food1_14 == True:
            food1_14 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 30 and pacman.y <= 60 and food1_15 == True:
            food1_15 = False
            score += 1
        #row2
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=90 and pacman.y<=120  and food2_1 == True:
            food2_1 = False
            score+=1
        if pacman.x >= 210 and pacman.x <= 240 and pacman.y >= 90 and pacman.y <= 120 and food2_4 == True:
            food2_4 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 90 and pacman.y <= 120 and food2_6 == True:
            food2_6 = False
            score += 1
        if pacman.x >= 450 and pacman.x <= 480 and pacman.y >= 90 and pacman.y <= 120 and food2_8 == True:
            food2_8 = False
            score += 1
        if pacman.x >= 570 and pacman.x <= 600 and pacman.y >= 90 and pacman.y <= 120 and food2_10 == True :
            food2_10 = False
            score += 1
        if pacman.x >= 690 and pacman.x <= 720 and pacman.y >= 90 and pacman.y <= 120 and food2_12 == True:
            food2_12 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 90 and pacman.y <= 120 and food2_15 == True:
            food2_15 = False
            score += 1
        #row3
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=150 and pacman.y<=180  and food3_1 == True:
            food3_1 = False
            score+=1
        if pacman.x >= 90 and pacman.x <= 120 and pacman.y >= 150 and pacman.y <= 180 and food3_2 == True:
            food3_2 = False
            score += 1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 150 and pacman.y <= 180 and food3_3 == True:
            food3_3 = False
            score += 1
        if pacman.x >= 210 and pacman.x <= 240 and pacman.y >= 150 and pacman.y <= 180 and food3_4 == True:
            food3_4 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 150 and pacman.y <= 180 and food3_6 == True:
            food3_6 = False
            score += 1
        if pacman.x >= 450 and pacman.x <= 480 and pacman.y >= 150 and pacman.y <= 180 and food3_8 == True:
            food3_8 = False
            score += 1
        if pacman.x >= 570 and pacman.x <= 600 and pacman.y >= 150 and pacman.y <= 180 and food3_10 == True :
            food3_10 = False
            score += 1
        if pacman.x >= 690 and pacman.x <= 720 and pacman.y >= 150 and pacman.y <= 180 and food3_12 == True:
            food3_12 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 150 and pacman.y <= 180 and food3_13 == True:
            food3_13 = False
            score += 1
        if pacman.x >= 810 and pacman.x <= 840 and pacman.y >= 150 and pacman.y <= 180 and food3_14 == True:
            food3_14 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 150 and pacman.y <= 180 and food3_15 == True:
            food3_15 = False
            score += 1
        #row4
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=210 and pacman.y<=240  and food4_1 == True:
            food4_1 = False
            score+=1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 210 and pacman.y <=240 and food4_5 == True:
            food4_5 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 210 and pacman.y <=240 and food4_6 == True:
            food4_6 = False
            score += 1
        if pacman.x >= 390 and pacman.x <= 420 and pacman.y >= 210 and pacman.y <= 240 and food4_7 == True:
            food4_7 = False
            score += 1
        if pacman.x >= 450 and pacman.x <= 480 and pacman.y >= 210 and pacman.y <= 240 and food4_8 == True:
            food4_8 = False
            score += 1
        if pacman.x >= 510 and pacman.x <= 540 and pacman.y >= 210 and pacman.y <= 240 and food4_9 == True:
            food4_9 = False
            score += 1

        if pacman.x >= 570 and pacman.x <= 600 and pacman.y >= 210 and pacman.y <= 240 and food4_10 == True :
            food4_10 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 210 and pacman.y <= 240 and food4_11 == True:
            food4_11 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 210 and pacman.y <=240 and food4_15 == True:
            food4_15 = False
            score += 1
        #row5
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=270 and pacman.y<=300  and food5_1 == True:
            food5_1 = False
            score+=1
        if pacman.x >= 90 and pacman.x <= 120 and pacman.y >= 270 and pacman.y <= 300 and food5_2 == True:
            food5_2 = False
            score += 1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 270 and pacman.y <= 300 and food5_3 == True:
            food5_3 = False
            score += 1
        if pacman.x >= 210 and pacman.x <= 240 and pacman.y >= 270 and pacman.y <= 300 and food5_4 == True:
            food5_4 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 270 and pacman.y <= 300 and food5_5 == True:
            food5_5 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 270 and pacman.y <= 300 and food5_11 == True:
            food5_11 = False
            score += 1
        if pacman.x >= 690 and pacman.x <= 720 and pacman.y >= 270 and pacman.y <=300 and food5_12 == True:
            food5_12 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 270 and pacman.y <= 300 and food5_13 == True:
            food5_13 = False
            score += 1
        if pacman.x >= 810 and pacman.x <= 840 and pacman.y >= 270 and pacman.y <= 300 and food5_14 == True:
            food5_14 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 270 and pacman.y <= 300 and food5_15 == True:
            food5_15 = False
            score += 1
        #row6
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=330 and pacman.y<=360  and food6_1 == True:
            food6_1 = False
            score+=1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 330 and pacman.y <=360 and food6_3 == True:
            food6_3 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 330 and pacman.y <= 360 and food6_5 == True:
            food6_5 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 330 and pacman.y <= 360 and food6_11 == True:
            food6_11 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 330 and pacman.y <= 360 and food6_13 == True:
            food6_13 = False
            score += 1
        if pacman.x >= 810 and pacman.x <= 840 and pacman.y >= 330 and pacman.y <= 360 and food6_14 == True:
            food6_14 = False
            score += 1
        #row7
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=390 and pacman.y<=420  and food7_1 == True:
            food7_1 = False
            score+=1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 390 and pacman.y <=420 and food7_3 == True:
            food7_3 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 390 and pacman.y <= 420 and food7_5 == True:
            food7_5 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 390 and pacman.y <= 420 and food7_11 == True:
            food7_11 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 390 and pacman.y <= 420 and food7_13 == True:
            food7_13 = False
            score += 1
        #row8
        if pacman.x >= 30 and pacman.x<=60 and pacman.y>=450 and pacman.y<=480  and food8_1 == True:
            food8_1 = False
            score+=1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 450 and pacman.y <=480 and food8_3 == True:
            food8_3 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 450 and pacman.y <= 480 and food8_5 == True:
            food8_5 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 450 and pacman.y <= 480 and food8_11 == True:
            food8_11 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 450 and pacman.y <= 480 and food8_13 == True:
            food8_13 = False
            score += 1
        if pacman.x >= 810 and pacman.x <= 840 and pacman.y >= 450 and pacman.y <= 480 and food8_14 == True:
            food8_14 = False
            score += 1
        #row9
        if pacman.x >= 30 and pacman.x <= 60 and pacman.y >= 510 and pacman.y <= 540 and food9_1 == True:
            food9_1 = False
            score += 1
        if pacman.x >= 90 and pacman.x <= 120 and pacman.y >= 510 and pacman.y <= 540 and food9_2 == True:
            food9_2 = False
            score += 1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 510 and pacman.y <= 540 and food9_3 == True:
            food9_3 = False
            score += 1
        if pacman.x >= 210 and pacman.x <= 240 and pacman.y >= 510 and pacman.y <= 540 and food9_4 == True:
            food9_4 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 510 and pacman.y <=540 and food9_5 == True:
            food9_5 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 510 and pacman.y <=540 and food9_6 == True:
            food9_6 = False
            score += 1
        if pacman.x >= 390 and pacman.x <= 420 and pacman.y >= 510 and pacman.y <=540 and food9_7 == True:
            food9_7 = False
            score += 1
        if pacman.x >= 450 and pacman.x <= 480 and pacman.y >= 510 and pacman.y <= 540 and food9_8 == True:
            food9_8 = False
            score += 1
        if pacman.x >= 510 and pacman.x <= 540 and pacman.y >= 510 and pacman.y <= 540 and food9_9 == True:
            food9_9 = False
            score += 1

        if pacman.x >= 570 and pacman.x <= 600 and pacman.y >= 510 and pacman.y <= 540 and food9_10 == True :
            food9_10 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 510 and pacman.y <= 540 and food9_11 == True:
            food9_11 = False
            score += 1
        if pacman.x >= 690 and pacman.x <= 720 and pacman.y >= 510 and pacman.y <=540 and food9_12 == True:
            food9_12 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 510 and pacman.y <=540 and food9_13 == True:
            food9_13 = False
            score += 1
        if pacman.x >= 810 and pacman.x <= 840 and pacman.y >= 510 and pacman.y <= 540 and food9_14 == True:
            food9_14 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 510 and pacman.y <= 540 and food9_15 == True:
            food9_15 = False
            score += 1
        #row10
        if pacman.x >= 30 and pacman.x <= 60 and pacman.y >= 570 and pacman.y <= 600 and food10_1 == True:
            food10_1 = False
            score += 1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 570 and pacman.y <= 600 and food10_3 == True:
            food10_3 = False
            score += 1
        if pacman.x >= 210 and pacman.x <= 240 and pacman.y >= 570 and pacman.y <= 600 and food10_4 == True:
            food10_4 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 510 and pacman.y <=600 and food10_5 == True:
            food10_5 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 570 and pacman.y <=600 and food10_6 == True:
            food10_6 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 570 and pacman.y <= 600 and food10_11 == True:
            food10_11 = False
            score += 1
        if pacman.x >= 690 and pacman.x <= 720 and pacman.y >= 570 and pacman.y <=600 and food10_12 == True:
            food10_12 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 570 and pacman.y <=600 and food10_13 == True:
            food10_13 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 570 and pacman.y <= 600 and food10_15 == True:
            food10_15 = False
            score += 1
        #row11
        if pacman.x >= 30 and pacman.x <= 60 and pacman.y >= 630 and pacman.y <= 660 and food11_1 == True:
            food11_1 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 630 and pacman.y <=660 and food11_5 == True:
            food11_5 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 630 and pacman.y <=660 and food11_6 == True:
            food11_6 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 630 and pacman.y <= 660 and food11_11 == True:
            food11_11 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 630 and pacman.y <= 660 and food11_15 == True:
            food11_15 = False
            score += 1
        #row12
        if pacman.x >= 30 and pacman.x <= 60 and pacman.y >= 690 and pacman.y <= 720 and food12_1 == True:
            food12_1 = False
            score += 1
        if pacman.x >= 90 and pacman.x <= 120 and pacman.y >= 690 and pacman.y <= 720 and food12_2 == True:
            food12_2 = False
            score += 1
        if pacman.x >= 150 and pacman.x <= 180 and pacman.y >= 690 and pacman.y <= 720 and food12_3 == True:
            food12_3 = False
            score += 1
        if pacman.x >= 210 and pacman.x <= 240 and pacman.y >= 690 and pacman.y <= 720 and food12_4 == True:
            food12_4 = False
            score += 1
        if pacman.x >= 270 and pacman.x <= 300 and pacman.y >= 690 and pacman.y <=720 and food12_5 == True:
            food12_5 = False
            score += 1
        if pacman.x >= 330 and pacman.x <= 360 and pacman.y >= 690 and pacman.y <=720 and food12_6 == True:
            food12_6 = False
            score += 1
        if pacman.x >= 630 and pacman.x <= 660 and pacman.y >= 690 and pacman.y <= 720 and food12_11 == True:
            food12_11 = False
            score += 1
        if pacman.x >= 690 and pacman.x <= 720 and pacman.y >= 690 and pacman.y <=720 and food12_12 == True:
            food12_12 = False
            score += 1
        if pacman.x >= 750 and pacman.x <= 780 and pacman.y >= 690 and pacman.y <=720 and food12_13 == True:
            food12_13 = False
            score += 1
        if pacman.x >= 810 and pacman.x <= 840 and pacman.y >= 690 and pacman.y <= 720 and food12_14 == True:
            food12_14 = False
            score += 1
        if pacman.x >= 870 and pacman.x <= 900 and pacman.y >= 690 and pacman.y <= 720 and food12_15 == True:
            food12_15 = False
            score += 1




        if count4 == 80:
            print("1")
        if count4 == 160:
            print("2")
        if count4 == 240:
            print("3")
        if count4 == 320:
            print("4")
        if count4 == 400:
            print("start")
            count4+=1



if __name__ =="__main__":
    mainloop()
