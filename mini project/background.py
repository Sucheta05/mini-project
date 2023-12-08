import pygame
from image import *

width=800
height=600
screen=pygame.display.set_mode((width,height))
def background():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(400,0))
    screen.blit(yellow_strip,(400,100))
    screen.blit(yellow_strip,(400,200))
    screen.blit(yellow_strip,(400,300))
    screen.blit(yellow_strip,(400,400))
    screen.blit(yellow_strip,(400,500))
    screen.blit(yellow_strip,(400,600))
    screen.blit(strip,(120,0))
    screen.blit(strip,(680,0))