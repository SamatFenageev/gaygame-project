import pygame, sys
pygame.init()
window=pygame.display.set_mode((1500, 800))
background=pygame.Surface((window.get_rect().width, window.get_rect().height))
background.fill((87,185,255))
image=pygame.image.load('kukuruz.bmp')
image=image.convert()
image2=pygame.image.load('kukuruz.bmp')
image2=image2.convert_alpha()
rect=image.get_rect()
rect2=image2.get_rect()
rect2.left=rect.width+1
i=255
while True:
    for event in pygame.event.get():
        if event.type==12:
            pygame.quit()
            sys.exit()
    image.set_alpha(i)
    image2.set_alpha(i)
    window.fill((87,185,255))
    window.blit(background, background.get_rect())
    window.blit(image, rect)
    window.blit(image2, rect2)
    pygame.time.delay(20)
    i-=3
    if i==0:
        i=255
    pygame.display.update()
