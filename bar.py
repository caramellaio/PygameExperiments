import pygame
import math

class CmdBar():
  
    def __init__(self,dim_x,dim_y,pos_x,pos_y,surf,active=False,text=""):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((dim_x,dim_y))        
        #pygame.draw.circle(self.image, (255,0,0), (50,50), 50, 2)
        self.image.fill((0,100,0))
        self.rect = self.image.get_rect()
        self.event_dict = dict()
        self.x = pos_x
        self.y = pos_y
        self.active = active
        self.font = pygame.font.Font("digital.ttf",25)
        self.parent_surf = surf
        self.text = "" 
        self._max_size = self.get_max_char_space()

    #still not drawing cursor
    def draw(self,text=None,cursor_pos=None):
        if text == None: text = self.text
        if cursor_pos == None: cursor_pos = len(text)
        if(self.active):
            self.write_text(text)
            self._draw_cursor(cursor_pos,(110,10,10))
        else:
            self.image.fill((0,0,0))
        self.parent_surf.blit(self.image,(self.x,self.y))
    
    def _draw_cursor(self,cursor_pos,cursor_color):
        char_sz = self.font.render("a",1,(2,2,2)).get_size()
        start_x = char_sz[0]*cursor_pos
        start_y = 0 # could be wrong...
        size_x = char_sz[0]#start_x + char_sz[0]
        size_y = char_sz[1]
        pygame.draw.rect(self.image,cursor_color,(start_x,start_y,size_x,size_y))

    def append_text(self, text):
        self.write_text(self.text+text if not self._max_size > len(self.text+text)  else text)
    
    def write_text(self,text):
        self.image.fill((0,0,0))
        if len(text) > self._max_size:
            text = text[self._max_size:]
        txt = self.font.render(text,1,(120,120,120))
        self.text = text
        self.image.blit(txt,(0,0))
        

    def set_font(self,font,size):
        self.font = pygame.font.Font(font,size)


    def get_max_char_space(self):
        size_chr = self.font.render("a",1,(2,2,2)).get_size()[0]
        return int(self.image.get_size()[0] / size_chr)


