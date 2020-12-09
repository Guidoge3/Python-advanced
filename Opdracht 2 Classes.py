import sys
import pygame
from pygame.locals import *
import random

class Babroi(Characters):

    Lives = 4
    Speed = 25
    Points = 0
    item = None

    def __init__(self):
        #Constructor functie.

    def Walk(self):
        super().Walk()
        #instructies lopen.

    def die(self):
        #dood

Babroi1 = Babroi()
Babroi2 = Babroi()
Babroi1.points += 15
Babroi2.Walk()


class enemy(Characters):
    
    Lives = 1
    Speed = 13
    Points = 15
    
    def __init__(self):
        #constructor
    
    def Walk(self):
        #lopen

    def die(self):
        #dood

enemy1 = enemy()
enemy2 = enemy()
enemy1.points -= 15
enemy2.Walk()

class Characters:

    Speed = 25
    sprite = ###
    Points = 15

Walk(self):
    #waggelen
die(self):
    #dood

