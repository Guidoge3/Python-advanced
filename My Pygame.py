import sys
import pygame
import math
from pygame.locals import *


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("My pygame")

Scherm_breedte = 1400
Scherm_hoogte = 800

Screensize = [Scherm_breedte, Scherm_hoogte]
Scherm = pygame.display.set_mode(Screensize)

KEYDOWN = []

Clock = pygame.time.Clock()
FPS = 60 
Achtergrond_kleur = [0, 0, 0]

IsRunning = True

#Enemy = pygame.image.load("..\Python advanced\Art\EnemyAlien.png")

PlayerSprite = pygame.image.load("..\Python advanced\Art\space-ship.png")
playerRect = PlayerSprite.get_rect()
PlayerSpeed = 3.5

class Coins :
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("..\Python advanced\Art\Bitcoin.png")
        self.rect = self.image.get_rect()

CoinAmount = 25

#staat er helaas nog niet in als bruikbaar item maar komt nog wel.^

while IsRunning:

    KEYDOWN = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            IsRunning = False
    
    if (KEYDOWN[K_w]):
        playerRect.y -= PlayerSpeed
    elif (KEYDOWN[K_s]):
        playerRect.y += PlayerSpeed

    if (KEYDOWN[K_a]):
        playerRect.x -= PlayerSpeed
    elif (KEYDOWN[K_d]):
        playerRect.x += PlayerSpeed

    Scherm.fill(Achtergrond_kleur)

    Scherm.blit(PlayerSprite, playerRect)

    pygame.display.flip()

    Clock.tick(FPS)

    