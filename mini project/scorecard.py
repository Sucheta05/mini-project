import pygame

width=800
height=600
screen=pygame.display.set_mode((width,height))
def score_card(car_passed,score):
    font=pygame.font.SysFont(None,35)
    passed=font.render("Passed:"+str(car_passed),True,(255,255,255))
    score=font.render("Score:" +str(score),True,(0,0,0))
    screen.blit(passed,(0,50))
    screen.blit(score,(0,100))