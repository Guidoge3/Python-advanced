import sys
import pygame
from pygame.locals import *
import random
import time

class Babroi:

    Lives = 4
    Speed = 25
    Points = 5
    item = None

    def __init__(self):
        #Constructor functie.
        self.Speed = 25
        print("Babroi is created out of atoms!")

    def Walk(self):
        print("snelheid van Babroi:", self.Speed)

    def die (self):
        print("Babroi is dood gegaan")
    

    def levenserbij (self):
        if (Babroi.Points == 100):
            Babroi.Lives += 1

        elif (Babroi1.Points != 100):
            while True:
                time.sleep(5)
                print("points is: ", Babroi1.Points)

Babroi1 = Babroi()
Babroi2 = Babroi()
Babroi1.Points += 15
Babroi2.Walk()


class enemy(Babroi):
        
    Points = 3

    def __init__(self, Speed, Lives):
        self.Speed = super().Speed
        self.Lives = super().Lives
        print("enemy is ontstaan")
        #constructor

    def Walk(self, newSpeed):
        # newspeed = self.Speed
        print("enemy loopt met snelheid: ", newSpeed)

enemy1 = enemy(15, 1)
enemy2 = enemy(5, 3)
enemy1.Walk(3)

print(Babroi1.Points)
print(Babroi1.Speed)
print(Babroi1.Lives)
print(Babroi1.Points)
print(enemy1.Walk(3))