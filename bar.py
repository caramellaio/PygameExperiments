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
        self.text = text
        self.font = pygame.font.SysFont("monospace",25)
        self.parent_surf = surf
        self.cmd_dict = self.load_cmd_dict()
        self._something_changes = False
        self.text_history = TextManager()
    
    def set_pos(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        if(self._something_changes):
            if(self.active):
                self.write_text(self.text)
            else:
                self.image.fill((0,0,0))
            self.parent_surf.blit(self.image,(self.x,self.y))
            self._something_changes = False

    def append_text(self, text):
        self._something_changes = True
        self.write_text(self.text+text if self._get_max_text_capacity() > len(text+self.text) else text)
    
    def write_text(self,text):
        self.text_history
        self._something_changes = True
        self.image.fill((0,0,0))
        txt = self.font.render(text,1,(120,120,120))
        print(text)
        self.text = text
        self.image.blit(txt,(0,0))
        

    def set_font(self,font,size):
        self.font = pygame.font.Font(font,size)

    def apply_special_keys(self,keys):
        for key in keys:
            self.cmd_dict[key]()

    def load_cmd_dict(self):
        el =dict()
        
        el[96] = self.change_status
        el[8] = lambda: self.write_text(self.text[:-1]) 
        el[274] = lambda: (self.text_history.move_down().get_actual_elem())
        #el[8] = 
        return el


    def read_command(self,text):
        pass

    def change_status(self):
        self._something_changes = True
        self.close_bar() if self.active else self.open_bar()

    def close_bar(self):
        self.active = False
 #       self.parent_surf.fill((0,0,0))
        self.write_text("")
        self.image.fill((0,0,0))
        print("bar closed")

    def open_bar(self):
        self.active = True

    def get_event(self,ev):
        if(ev.key in self.cmd_dict):
            self.cmd_dict[ev.key]()
        elif self.active:
            self.append_text(chr(ev.key))

    # TODO: fix
    def _get_max_text_capacity(self):
        size = self.font.render("a",1,(2,2,2)).get_size()[0]
        return math.floor(self.image.get_size()[0] / size)


class TextManager(list):
    def __init__(self):
        super()
        self._actual_index = 0

    def move_up(self):
        self._actual_index -= int(self._actual_index > 0)
        return self

    def move_down(self):
        self._actual_index += 1
        return self
   
    def get_actual_elem(self):
        return self[self._actual_index]

    def set_actual_elem(self,value):
        self[self._actual_index] = value
        return self