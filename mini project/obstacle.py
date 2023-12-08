import pygame
width=800
height=600
screen=pygame.display.set_mode((width,height))
def obstacle(obs_x,obs_y,obs):
    if obs==0:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car3.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car7.jpg")
    screen.blit(obs_pic,(obs_x,obs_y))   
    