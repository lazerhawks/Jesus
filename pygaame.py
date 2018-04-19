import pygame
import sys

SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 20


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Circles')
fps = pygame.time.Clock()
paused = False

ball_pos1 = [290, 140]
p=True
r=0
e=1
def update():
    global e
    global r
    if(e==1):
        ball_pos1[0]-=1
        ball_pos1[1]+=1
        r+=1
    
    if(e==2):
        ball_pos1[0]+=1
        ball_pos1[1]+=1
        r+=1

    if(e==3):
        ball_pos1[0]+=1
        ball_pos1[1]-=1
        r+=1
    if(e==4):
        ball_pos1[0]-=1
        ball_pos1[1]-=1
        r+=1
    if(r>=45 and e<5):
        r=0
        e+=1
    if(e>=5):
        e=1
    


def render():
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, ball_pos1, CIRCLE_RADIUS, 0)
    pygame.display.update()
    fps.tick(60)
c=0
t=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                paused = not paused
    if not paused:
        update()
        render()
        if(CIRCLE_RADIUS<50 and p==True):
            CIRCLE_RADIUS+=1
            c+=1
        elif(CIRCLE_RADIUS>20 and p==False):
            CIRCLE_RADIUS-=1
            c-=1
        if(c>15):
            p=False
        t+=1
        if(t>30):
            t=0
            c=0
            p=True
        
        
        
            
        
    
        
