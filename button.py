import pygame
import pygame.font
from random import randint
#from time import sleep
class Button():
    def __init__(self,sc,msg,posx,posy):
        self.msg=msg
        self.sc=sc
        self.posx=posx
        self.posy=posy
        self.width,self.height=200,100
        #||||||||||||||||||||||||
        self.text_color=(255,255,255)
        self.button_color=(252,195,0)
        self.font=pygame.font.SysFont(None,48)
        self.msg_image=self.font.render(msg,True,self.text_color,
                                        None)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx=self.posx
        self.rect.centery=self.posy
        self.msg_rect=self.msg_image.get_rect()
        self.msg_rect.centerx=self.rect.centerx
        self.msg_rect.centery=self.rect.centery
        #\\\ROUNDed corners\\\
        self.r=30
    def draw_button(self):
        #Just rects
        self.sc.fill(self.button_color,self.rect)
        #making rounded corners(topleft->topright->bottomright->bottomleft)
        pygame.draw.circle(self.sc,self.button_color,self.rect.topleft,self.r)
        pygame.draw.circle(self.sc,self.button_color,self.rect.topright,self.r)
        pygame.draw.circle(self.sc,self.button_color,self.rect.bottomright,self.r)
        pygame.draw.circle(self.sc,self.button_color,self.rect.bottomleft,self.r)
        #turning kinda shit into a rounded rect:)
        #left
        pygame.draw.rect(self.sc,self.button_color,(self.rect.x-self.r,self.rect.y,
                                                    self.r,self.height))
        #top
        pygame.draw.rect(self.sc,self.button_color,(self.rect.x,self.rect.y-self.r,
                                                    self.width,self.r))
        #right
        pygame.draw.rect(self.sc,self.button_color,(self.rect.x+self.width,self.rect.y,
                                                    self.r,self.height))
        #bottom
        pygame.draw.rect(self.sc,self.button_color,(self.rect.x,self.rect.y+self.height,
                                                    self.width,self.r))
        self.sc.blit(self.msg_image,self.msg_rect)
        #sleep(0.13)
