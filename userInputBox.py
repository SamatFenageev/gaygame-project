import pygame as pg
pg.init()
COLOR_INACTIVE = (0,0,0,)
COLOR_ACTIVE = (255,0,0)
FONT = pg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, screen, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.info=FONT.render('If you want to change the face, type direction to the file, where it\'s located'
                                  ,True,(255,255,255))        
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
##                    self.returningText=self.text
##                    try:
##                    pers.face=pg.image.load(self.text)
                    
##                    except:
                    self.text = ''
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key==pg.K_RETURN:
                    """write your updates underneath..."""
                    retText=self.text
                    self.text+=''
                    return retText
                else:
                    self.text += event.unicode      #you can also use self.text+=event.key(to check what key the user typed), BUT
                                                    #ascii symbols won't appear
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
        

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.info, (self.rect.x,self.rect.y-25))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
