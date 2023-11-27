import pygame 
from laser import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,constraint,speed):

    def get_input(self):

    def recharge(self):

    def constraint(self):

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))

    def update(self):

