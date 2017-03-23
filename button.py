import pygame

class Button(pygame.sprite.Sprite):
    BUTTON_PATH="button.png"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))        
        pygame.draw.circle(self.image, (255,0,0), (50,50), 50, 2)
        self.rect = self.image.get_rect()
        self.event_dict = dict()
        self.x = self.rect.topleft[0]
        self.y = self.rect.topleft[1]

    def set_pos(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self,surface):
        surface.blit(self.image,(self.x,self.y))

    def update(self,h):
        pass

    def onevent(self,event):
        if(event in self.event_dict):
            self.event_dict[event][0](*self.event_dict[event][1:])

    def add_event_func(self,event,func,params):
        self.event_dict[event] = []
        self.event_dict[event].append(func)
        self.event_dict[event].extend(params)

