import pygame
class PressSth():
    def __init__(self,sc):
        self.sc=sc
        self.sc_rect=self.sc.get_rect()
        self.font=pygame.font.SysFont(None,32)
        self.text=self.font.render('Press F to show who\'s is GAY here :3',True,(255,255,255),(0,0,0))
        self.rect=self.text.get_rect()
        self.rect.centerx=self.sc_rect.centerx
        self.rect.bottom=self.sc_rect.bottom-15

    def blitme(self):
        self.sc.blit(self.text,self.rect)
