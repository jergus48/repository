import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()

WIDTH = 350
HEIGHT=600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

birdheight=50
birdwidth=50
FPS=60
pygame.display.set_caption("flappy bird")

back= pygame.transform.scale(pygame.image.load(
        os.path.join('Assets', 'flappybg.png')), (WIDTH, HEIGHT))

scorefont=pygame.font.SysFont('comicsans', 50)

bird_image = pygame.image.load(
    os.path.join('Assets', 'flappy.png'))
white=(255,255,255)
flappybird= pygame.transform.scale(
    bird_image, (birdwidth, birdheight))


def draw_window(bird,up,down,wallsdole1,wallshore1,score):
    WIN.blit(back, (0, 0))
    WIN.blit(flappybird, (bird.x, bird.y))

    WIN.blit(wallsdole1, (down.x, down.y))
    WIN.blit(wallshore1, (up.x, 0))

    score_text = scorefont.render(
        "Score: " + str(score), 1, white)
    WIN.blit(score_text, (5, 10))


    pygame.display.update()

def new_game(down,up,bird,score):


    score_text2 = scorefont.render(
        "Try again", 1, white)
    WIN.blit(score_text2, (70, 80))
    score_text2 = scorefont.render(
        "Press r to restart", 1, white)
    WIN.blit(score_text2, (10, 115))

    pygame.display.update()

    bird.y-=3
    if score<=50:
        down.x += 5
        up.x += 5
    if score>=50:
        down.x += 6
        up.x += 6

def restart():
    mainloop()




def mainloop():
    wallhore_IMAGE = pygame.image.load(
        os.path.join('Assets', 'flappy+walls.png'))
    wallshore1 = pygame.transform.rotate(pygame.transform.scale(
        wallhore_IMAGE, (40, 150)), 180)

    wallsdole_IMAGE = pygame.image.load(
        os.path.join('Assets', 'flappy+walls.png'))
    wallsdole1 = pygame.transform.scale(
        wallsdole_IMAGE, (40, 150))
    clock = pygame.time.Clock()
    run = True
    run2=True
    horne = []
    dolne = []
    score=0
    bird = pygame.Rect(125, 250, birdwidth, birdheight)
    up=pygame.Rect(380, 0, 40, 50)
    horne.append(up)
    down = pygame.Rect(380, 550, 40, 50)
    dolne.append(down)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if run2==True:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        bird.y -=60
        bird.y += 3

        if up.x and down.x<=-30:
            horne.remove(up)
            dolne.remove(down)
            score+=1
        if len(horne)<=1:
            y=["1","2","3"]
            x = random.choice(y)
            if x == "1":
                wallshore1 = pygame.transform.rotate(pygame.transform.scale(
                    wallhore_IMAGE, (40, 237)),180)
                up=pygame.Rect(380, 0, 40, 237)
                horne.append(up)
            elif x == "2":
                wallshore1 = pygame.transform.rotate(pygame.transform.scale(
                    wallhore_IMAGE, (40, 197)),180)
                up=pygame.Rect(380, 0, 40, 197)
                horne.append(up)
            elif x == "3":
                wallshore1 = pygame.transform.rotate(pygame.transform.scale(
                    wallhore_IMAGE, (40, 227)),180)
                up=pygame.Rect(380, 0, 40, 227)
                horne.append(up)
        if len(dolne)<=1:
            y = ["1", "2", "3"]
            x = random.choice(y)
            if x == "1":
                wallsdole1 = pygame.transform.scale(
                    wallsdole_IMAGE, (40, 177))
                down = pygame.Rect(380, 420, 40, 177)
                dolne.append(down)
            elif x == "2":
                wallsdole1 = pygame.transform.scale(
                    wallsdole_IMAGE, (40, 197))
                down = pygame.Rect(380, 400, 40, 197)
                dolne.append(down)
            elif x == "3":
                wallsdole1 = pygame.transform.scale(
                    wallsdole_IMAGE, (40, 227))
                down = pygame.Rect(380, 370, 40,227)
                dolne.append(down)

        draw_window(bird,up,down,wallsdole1,wallshore1,score)
        if bird.colliderect(up):
            new_game( down, up,bird,score)
            run2=False
        if bird.colliderect(down):
            new_game( down, up,bird,score)
            run2 = False

        if bird.y>= 600:
            new_game(down,up,bird,score)
            run2 = False
        if bird.y<= 0:
            new_game(down,up,bird,score)
            run2 = False
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_r]:
            restart()
        if score<=50:
            down.x -= 5
            up.x -= 5
        if score>=50:
            down.x -= 6
            up.x -= 6



    mainloop()
if __name__ =="__main__":
    mainloop()

