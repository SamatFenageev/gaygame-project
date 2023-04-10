import pygame
class Person():
    def __init__(self,sc):
        #screen
        self.sc=sc
        self.sc_rect=self.sc.get_rect()
        self.face=pygame.image.load('face.bmp')
        self.body=pygame.image.load('player.bmp')
        self.create_a_person()
        #screen
        #movin flags
        self.moving_right=False
        self.moving_left=False
        self.x=self.bodyRect.centerx
        self.faceX=self.rect.centerx
    def update(self):
        if self.moving_right and self.bodyRect.right<self.sc_rect.right:
            self.x+=4.0
            self.faceX+=4.0
        if self.moving_left and self.bodyRect.left>0:
            self.x-=4.0
            self.faceX-=4.0
        self.rect.centerx=self.faceX
        self.bodyRect.centerx=self.x
    def create_a_person(self,face=pygame.image.load('face.bmp')):
        #face
        
        self.strechedFace=pygame.transform.scale(self.face,(self.sc_rect.width//16,self.sc_rect.height//9))
        self.rect=self.strechedFace.get_rect()
    #face
        self.strechedImg=pygame.transform.scale(self.body,(self.sc_rect.width//16,self.sc_rect.height//9))
        self.bodyRect=self.strechedImg.get_rect()
#coords
        self.bodyRect.centerx=self.sc_rect.centerx
        self.bodyRect.bottom=self.sc_rect.bottom
        ###################################
        self.rect.centerx=self.bodyRect.centerx
        self.rect.centery=self.bodyRect.y
        ###################################
    def blitme(self):
        self.sc.blit(self.strechedFace,self.rect)
        self.sc.blit(self.strechedImg,self.bodyRect)
