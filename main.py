import pygame
from data import *
from shooter import *

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Shooter")

def run():
    dame = True

    hero = Hero(100, 100, 100, 100, speed= 5, color= (23,114, 9))
    clock = pygame.time.Clock()
    
    while game:
        window.fill((255,255,255))

        hero.move()
        pygame.draw.rect(window, hero.COLOR, hero)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    hero.MOVE["Down"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_w:
                    hero.MOVE["RIGHT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                if event.key == pygame.K_w:
                    hero.MOVE["DOWN"] = False
                if event.key == pygame.K_w:
                    hero.MOVE["LEFT"] = False
                if event.kty == pygame.K_w:
                    hero.MOVE["RIGHT"] = False

        clock.tick(60)
        pygame.display.flip()

run()