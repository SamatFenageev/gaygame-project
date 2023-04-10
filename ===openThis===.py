import pygame
from pygame.sprite import Group
from person import Person
import gay_gf as gf
from intro import Intro
from press import PressSth
from button import Button
from scoreboard import Scoreboard
#|||||||||||
from pygame import mixer
mixer.init()
song = mixer.music.load('nana.mp3')#('shots&squats.mp3')
#|||||||||||||
#init-ing pygame
pygame.init()
#def-ing var-s
#open('score.txt').read()
sc=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
artem=Person(sc)
lollies=Group()
press=PressSth(sc)
intro=Intro(sc,press)
scoreboard=Scoreboard(sc,gf.CURRENT_SCORE,None)
#|||||||||||||||||||||||||||||||||
button1=Button(sc,'Simple Mode',sc.get_rect().centerx-180,sc.get_rect().centery)
button2=Button(sc,'Fun Mode',sc.get_rect().centerx+180,sc.get_rect().centery)
button3=Button(sc,'Store',sc.get_rect().centerx-180,sc.get_rect().centery+240)
button4=Button(sc,'Customize',sc.get_rect().centerx+180,sc.get_rect().centery+240)
#|||||||||||STARTING|||||||||||
intro.update()
while not gf.isRunning:
    press.blitme()
    gf.events(artem,sc,lollies,intro=intro,press=press)
"""btw you can't del(yet(23.02.2020)) var-s like press and
    intro cuz they're used further. GL boiii ;)"""
del press,intro
#YOU did it boiii, proud of you!)

store_img=pygame.image.load('Store.bmp')
while True:
    #mixer.music.play(1) #<<<<<<<<don't forget
    if gf.isInMenu:
        gf.show_menu(artem,sc,lollies,button1,button2,button3,button4)
        gf.events(artem,sc,lollies,button1,button2,button3,button4)
    elif gf.isSimpleMode:
        gf.simple_mode(artem,lollies,sc,scoreboard)
    elif gf.isFunMode:
        gf.fun_mode(artem,lollies,sc)
    elif gf.isStore:
        gf.is_store(artem,store_img,lollies,sc)
    elif gf.isCustomizing:
        gf.custome(artem,lollies,sc)
