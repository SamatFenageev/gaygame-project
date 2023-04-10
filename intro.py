import pygame

bg=(0,0,0)
class Intro():
    def __init__(self,sc,press):
        self.sc=sc
        self.press=press
        self.sc_rect=self.sc.get_rect()
        #self.image=pygame.image.load('kukuruz.bmp')
        self.image=pygame.image.load('GayIntro2.bmp').convert(self.sc)
        
        self.rect=self.image.get_rect()     
        self.rect.bottom=self.sc_rect.top
        self.rect.centerx=self.sc_rect.centerx
        self.y=float(self.rect.bottom)

    def blitme(self):
        self.sc.blit(self.image,self.rect)

    def update(self):
        while self.y<self.sc_rect.centery:
            self.y+=0.8
            self.rect.centery=self.y
            self.sc.fill(bg)
            #self.sc.fill((0,0,0))
            self.sc.blit(self.image,self.rect)
            pygame.display.flip()
        while self.y>self.sc_rect.centery-110:
            self.y-=0.7
            self.rect.centery=self.y
            self.sc.fill(bg)
            self.sc.blit(self.image,self.rect)
            pygame.display.flip()
        while self.y<self.sc_rect.centery:
            self.y+=0.5
            self.rect.centery=self.y
            self.sc.fill(bg)
            self.sc.blit(self.image,self.rect)
            self.press.blitme()
            pygame.display.flip()
        while self.y>self.sc_rect.centery-70:
            self.y-=0.6
            self.rect.centery=self.y
            self.sc.fill(bg)
            self.sc.blit(self.image,self.rect)
            self.press.blitme()
            pygame.display.flip()
        while self.y<self.sc_rect.centery:
            self.y+=1.2
            self.rect.centery=self.y
            self.sc.fill(bg)
            self.sc.blit(self.image,self.rect)
            self.press.blitme()
            pygame.display.flip()
