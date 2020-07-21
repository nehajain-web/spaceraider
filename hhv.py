import pygame
import random
import math
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption(" space Invaders")
icon=pygame.image.load('ufo.jpg')
pygame.display.set_icon(icon)
running=True
spaceimg=pygame.image.load('space.png')
backgroundimg=pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
space_x=370
space_y=500
space_change=0
alien_img=[]
alien_x=[]
alien_y=[]
alien_xchange=[]
alien_ychange=[]
num_of_alien=6
for i in range(num_of_alien):
    alien_img.append(pygame.image.load('alien.png'))
    alien_x.append(random.randint(0,735))
    alien_y.append(random.randint(50,150))
    alien_xchange.append(0.4)
    alien_ychange.append(30)

bullet_img=pygame.image.load('bullet.png')
bullet_x=0
bullet_y=480
bullet_xchange=0
bullet_ychange=3.5
bullet_state="ready"
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
text_x=10
text_y=10
def show_score(x,y):
    score=font.render("score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def space(x,y):
    screen.blit(spaceimg,(x,y))
def alien(x,y,i):
    screen.blit(alien_img[i],(x,y))
def bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x+16,y+10))
def collision(alien_x,alien_y,bullet_x,bullet_y):
    distance=math.sqrt((math.pow(bullet_x-alien_x,2))+(math.pow(bullet_y-alien_y,2)))
    if distance<30:
        return True
    else:
        return False
    


while running:
    screen.fill((0,0,0))
    screen.blit(backgroundimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                space_change=-3.5
            
            if event.key==pygame.K_RIGHT:
                space_change=3.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                space_change=0
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                     bullet_sound_sound=mixer.Sound('laser.wav')
                     bullet_sound_sound.play()
                    
                     bullet(space_x,bullet_y)
                     
            
    space_x=space_x+space_change
    if space_x<=0:
        space_x=0
    if space_x>=736:
        space_x=736

    for i in range(num_of_alien):
       alien(alien_x[i],alien_y[i],i)
        
        
        
       alien_x[i]=alien_x[i]+alien_xchange[i]
       if alien_x[i]<=0:
           
           alien_xchange[i]=0.4
           alien_y[i]+=alien_ychange[i]
       
       elif alien_x[i]>=736:
           alien_xchange[i]=-0.4
           alien_y[i]+=alien_ychange[i]
       iscollision=collision(alien_x[i],alien_y[i],bullet_x,bullet_y)
       if iscollision:
           explosion_sound=mixer.Sound('explosion.wav')
           explosion_sound.play()
           bullet_y=480
           bullet_state="ready"
           score_value+=1
           
          
        
        
   
    if bullet_y<=0:
        bullet_y=480
        bullet_state="ready"
    if bullet_state is "fire":
        bullet(space_x,bullet_y)
        bullet_y-=bullet_ychange
   
    
    space(space_x,space_y)
    show_score(text_x,text_y)
    pygame.display.update()

