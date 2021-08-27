import pygame
import os
import time
pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT=500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong game")


redhotu = pygame.mixer.Sound(os.path.join('Assets','redhot.mp3'))
MAX_BALLS=1
FPS = 60
background= pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'IMG_7371.jpg')), (WIDTH, HEIGHT))
black=(0,0,0)
white=(255,255,255)

palka_WIDTH, palka_HEIGHT = 15, 75

YELLOW_palka_IMAGE = pygame.image.load(
    os.path.join('Assets', 'a.png'))

YELLOW_palka = pygame.transform.scale(
    YELLOW_palka_IMAGE, (palka_WIDTH, palka_HEIGHT))
red_palka_IMAGE = pygame.image.load(
    os.path.join('Assets', 'b.png'))

red_palka = pygame.transform.scale(
    red_palka_IMAGE, (palka_WIDTH, palka_HEIGHT))

VEL=5
print("space=10 second pause")
print("r=restart")

scorefont=pygame.font.SysFont('comicsans', 40)

def draw_window(yellow,red,balls,redscore,yellowscore):

    WIN.blit(background,(0,0))



    red_score_text = scorefont.render(
        "Score: " + str(redscore), 1, white)
    yellow_score_text = scorefont.render(
        "Score: " + str(yellowscore), 1, white)
    WIN.blit(red_score_text, (WIDTH - red_score_text.get_width() - 10, 10))
    WIN.blit(yellow_score_text, (10, 10))

    WIN.blit(YELLOW_palka, (yellow.x, yellow.y))
    WIN.blit(red_palka, (red.x, red.y))

    for ball in balls:
        pygame.draw.ellipse(WIN, white, ball)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_w] and yellow.y  > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y  + yellow.height < HEIGHT:  # DOWN
        yellow.y += VEL





def red_handle_movement(keys_pressed, red):

    if keys_pressed[pygame.K_UP] and red.y > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y  + red.height< HEIGHT :  # DOWN
        red.y+= VEL


def pause():
    x=10
    time.sleep(x)


def reset():
    pygame.mixer.stop()
    mainloop()

    return redhotu
def hudba():
    redhotu.play()

def mainloop():
    hudba()
    yellow = pygame.Rect(50, 200, palka_WIDTH, palka_HEIGHT)
    red = pygame.Rect(825, 200, palka_WIDTH, palka_HEIGHT)
    yellowscore=0
    redscore=0
    balls=[]
    ballspeedy=5
    ballspeedx=5
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if len(balls)<MAX_BALLS:
            ball=pygame.Rect(450-15, 500-25, 15,15)
            balls.append(ball)
        ball.x-=ballspeedx
        ball.y-=ballspeedy

        if (ball.x+15)>WIDTH or ((ball.x+15)>WIDTH and ball.y<-55) or ((ball.x+15)>WIDTH and ball.y>550):
            yellowscore += 1
            if ball in balls:
               balls.remove(ball)
            yellowscore+=1
        if (ball.x-10)< 0 or ((ball.x+15)>WIDTH and ball.y<-55) or ((ball.x+15)>WIDTH and ball.y>550):
            redscore+=1
            if ball in balls:
                balls.remove(ball)
        if (ball.y +25)== 0 or (ball.y+15+5) ==500:
            ballspeedy*= -1
        if ball.colliderect(yellow) or ball.colliderect(red):
            ballspeedx*=-1







        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:

            pause()
        if keys_pressed[pygame.K_r]:
            reset()



        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        draw_window(yellow, red, balls, redscore, yellowscore)

if __name__ =="__main__":
    mainloop()
