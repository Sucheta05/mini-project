import pygame
from image import *
width=800
height=600
screen=pygame.display.set_mode((width,height))
def car(x,y):
    screen.blit(carimg,(x,y))
