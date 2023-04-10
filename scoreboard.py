import pygame
class Scoreboard():
    def __init__(self,sc,score,hscore):
        self.sc=sc
        self.hscore=hscore
        self.sc_rect=self.sc.get_rect()
        self.font=pygame.font.SysFont(None,40)
        self.score=score
        self.prep_score()
    def prep_score(self):
        self.img=self.font.render(str(self.score),True,(0,0,0),None)
        self.rect=self.img.get_rect()
        self.rect.x=self.sc_rect.width-self.rect.width-15
        self.rect.y=15
    def prep_hscore(self):
        self.h_score_img=self.font.render(self.hscore,True,(0,0,0),None)
        #self.                   #<<<<<<доделай
    def blitme(self):
        self.sc.blit(self.img,self.rect)
        
