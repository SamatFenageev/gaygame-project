import pygame
from lol import Lol
from random import randint
import sys
from time import sleep
from userInputBox import InputBox


isRunning=False
musicIsPlaying=True
isInMenu=True
isSimpleMode=False
isFunMode=False
isStore=False
isCustomizing=False


amount_of_lollies=25
points=15



score_file=open('score.txt')#открываем для чтения самого высокого счёта
HIGHEST_SCORE=score_file.read()#записываем в хаест ско(лол)
CURRENT_SCORE=0#текущий счёт
LEVEL=1
score_file.close()
###score_file=open('score.txt','w')
                                                                                                    ########(87,185,255)##############cool color
#funcs:
def events(pers,sc,lols,*buttons,intro=None,press=None):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            keydown(event,pers,sc,intro,press)
        elif event.type==pygame.KEYUP:
            keyup(event,pers,sc)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for button in buttons:
                check_Buttonclick_collision(button,mouse_x, mouse_y)

                
def keydown(event,pers,sc,intro,press):#,intro,press):
    global musicIsPlaying,isRunning,isInMenu,isSimpleMode,isFunMode,isStore,isCustomizing
    if event.key==pygame.K_RIGHT:
        pers.moving_right=True
    elif event.key==pygame.K_LEFT:
        pers.moving_left=True
    elif event.key==pygame.K_q:
        pygame.quit()
        sys.exit()
    elif event.key==pygame.K_p and musicIsPlaying:
        pygame.mixer.music.pause()
        musicIsPlaying=False
    elif event.key==pygame.K_p and not musicIsPlaying:
        pygame.mixer.music.unpause()
        musicIsPlaying=True
    elif not isRunning:
        if event.key==pygame.K_f:
            start_intro(sc,intro,press)
    elif event.key==pygame.K_ESCAPE:
        if isSimpleMode:
            isSimpleMode=False
        elif isFunMode:
            isFunMode=False
        elif isStore:
            isStore=False
        elif isCustomizing:
            isCustomizing=False
        isInMenu=True
            

def keyup(event,pers,sc):
    if event.key==pygame.K_RIGHT:
        pers.moving_right=False
    elif event.key==pygame.K_LEFT:
        pers.moving_left=False

def create_lollies(lollies,sc):
    global amount_of_lollies
    for i in range(amount_of_lollies):
        lol=Lol(sc)
        lollies.add(lol)

def check_collisions(pers,lollies,sc):
                                                                                                                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<переделай так, чтобы И засчитывались очки И объекты удалялись
    global amount_of_lollies,CURRENT_SCORE,LEVEL#,score_file
    if pygame.sprite.spritecollideany(pers,lollies):
        collisions=pygame.sprite.spritecollide(pers,lollies,True)
        CURRENT_SCORE+=(0.1*LEVEL)#ведение  счёта зависит от уровня LEVEL
        CURRENT_SCORE=round(CURRENT_SCORE,2)
        #score_file.write(str(SCORE))
    if len(lollies)==0:
        sleep(1.2)
        amount_of_lollies+=10
        create_lollies(lollies,sc)
        LEVEL+=1
##    return CURRENT_SCORE

def check_bottom(sc,lollies):
    for lol in lollies.sprites():
        if lol.rect.top>sc.get_rect().bottom:
           lol.rect.y=randint(-5000,0)

def start_intro(sc,intro,press):
    global isRunning
    i=255
    while i>0:
        #изменение прозрачности объекта
        intro.image.set_alpha(i)
        sc.fill((0,0,0))
        sc.blit(intro.image,intro.rect)
        i-=1
        pygame.display.update()
    r=1#радиус круга для интро
    a,b=(sc.get_rect().centerx)**2,(sc.get_rect().centery)**2#квадраты катетовпрямогольного треугольника
    G=(a+b)**0.5#гипотенуза треугольника
    while r<=G:
        pygame.draw.circle(sc,(87,185,255),
                           (sc.get_rect().centerx,sc.get_rect().centery),r)
        r+=1#скорость увеличения радиуса
        pygame.display.flip()
    isRunning=True

def check_mouse_pos_for_button(button):
    x,y=pygame.mouse.get_pos()
##    if button.rect.collidepoint(x,y):
    if x in range(button.rect.x-button.r,button.rect.x+button.width+button.r)\
       and y in range(button.rect.y-button.r,button.rect.y+button.height+button.r):
        button.button_color=(170,142,10)
    else:
        button.button_color=(252,195,0)

def show_menu(pers,sc,lols,*buttons):
    sc.fill((87,185,255))
    events(pers,sc,lols)
    for button in buttons:
        button.draw_button()
        check_mouse_pos_for_button(button)
    pygame.display.flip()

def check_Buttonclick_collision(button,mouse_x,mouse_y):
    global isInMenu,isSimpleMode,isFunMode,isStore,isCustomizing
##    print('im here')
##    print(mouse_x,mouse_y)
##    print('x:'+str(button.rect.x)+'\n'+'width:'+str(button.rect.width))
##    print('y:'+str(button.rect.y)+'\n'+'height:'+str(button.rect.height))
##    print(button.msg)
    if mouse_x in range(button.rect.x-button.r,button.rect.x+button.width+button.r) and mouse_y in range(button.rect.y-button.r,button.rect.y+button.height+button.r):
        if isInMenu and button.msg=='Simple Mode':
            isInMenu=False
            isSimpleMode=True
        elif isInMenu and button.msg=='Fun Mode':
            isInMenu=False
            isFunMode=True
        elif isInMenu and button.msg=='Store':
            isInMenu=False
            isStore=True
        elif isInMenu and button.msg=='Customize':
            isInMenu=False
            isCustomizing=True
    
def simple_mode(pers,lols,sc,scoreboard):
    global isInMenu,CURRENT_SCORE
    while not isInMenu:
        sc.fill((87,185,255))
        events(pers,sc,lols)
        pers.update()
        lols.update()
        check_bottom(sc,lols)
        lols.draw(sc)
        check_collisions(pers,lols,sc)
        #working with scoreboard
        scoreboard.score=CURRENT_SCORE
        scoreboard.prep_score()
        scoreboard.blitme()
        #working with scoreboard
        pers.blitme()
        pygame.display.flip()

def fun_mode(pers,lols,sc):
    global isInMenu
    while not isInMenu:
        sc.fill((87,185,255))
        events(pers,sc,lols)
#||||||||||||||||add smth HERE|||||||||||||||||||||||||||||||||||||||||        
        pygame.display.flip()
def is_store(pers,img,lols,sc):
    global isInMenu
    while not isInMenu:
        sc.blit(img,[0,0])
        events(pers,sc,lols)
#||||||||||||||||add smth HERE|||||||||||||||||||||||||||||||||||||||||
        pygame.display.flip()
def custome(pers,lols,sc):
    global isInMenu,isCustomizing
    
    box=InputBox(100,100,140,32,sc)
    
    while not isInMenu:
        sc.fill((87,185,255))
        #handling events
        #||||||||||||||||||||||||||||||||||||||||||
        for event in pygame.event.get():
            box.handle_event(event)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    isInMenu=True
                    isCustomizing=False
        #|||||||||||||||||||||||||||||||||||||||||||||
##        text=box.returningText
##        print(text)
        box.update()
        box.draw(sc)
        pers.blitme()
        pygame.display.flip()
