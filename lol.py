import pygame
from pygame.sprite import Sprite
from random import randint
class Lol(Sprite):
    def __init__(self,sc):
        super().__init__()
        self.sc=sc
        self.sc_rect=self.sc.get_rect()
        self.image=pygame.image.load('lolly.bmp')
        self.strechedImg=pygame.transform.scale(self.image,(self.sc_rect.width//16,self.sc_rect.height//9))
        self.rect=self.strechedImg.get_rect()
        self.rect.x=randint(10,self.sc_rect.width-self.rect.width-10)
        self.rect.y=randint(-7000,0)
    def blitme(self):
        self.sc.blit(self.strechedImg,self.rect)
    def update(self):
        self.rect.y+=2.1
