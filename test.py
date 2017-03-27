import pygame
from pygame.locals import *
import random
from button import Button
from bar import CmdBar
from keyboard import KeyHandler 
#temp
oldkey = None

def main():
    pygame.init()
    screen = pygame.display.set_mode((240,480))
    pygame.display.set_caption("Basic Pygame Program")
    pygame.font.init()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    font = pygame.font.Font(None,36)

    k_hand = KeyHandler()
    #group stuff
    Button.groups = pygame.sprite.Group()
    
    b = Button()
    kkk = test2(screen)
    testFunc(b)
    Button.groups.add(b)
    screen.blit(background,(0,0))
    pygame.display.flip()
    random.seed(4324)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                onmousepressed([b],pygame.MOUSEBUTTONUP)
            
            if event.type == pygame.KEYDOWN:
                k_hand.handle_key_down(event)
                kkk.draw(k_hand.text,k_hand.cursor_pos)

            if event.type == pygame.KEYUP:
                k_hand.handle_key_up(event)
            #background.blit(text,textpos)
            #screen.blit(background,(random.randint(0,1000),random.randint(0,1000)))
            #text = font.render("sieg heil",1,(10,10,10))
        b.draw(screen)
        kkk.draw()
        if k_hand.handle_on_clock():
            kkk.draw(k_hand.text,k_hand.cursor_pos)
        pygame.display.update()
       # screen.fill((0,0,0))

def onmousepressed(sprites,event):
    pos = pygame.mouse.get_pos()
    for el in[s for s in sprites if s.rect.collidepoint(pos)]:
        el.onevent(event)

def testFunc(b):
    b.add_event_func(pygame.MOUSEBUTTONUP,lambda b: b.set_pos(20,20) ,[b])

def test2(screen):
    return CmdBar(screen.get_size()[0],100,0,screen.get_size()[1] -110,screen,True,"a")
    #return  CmdBar(640,100,0,370,screen,True,"hola")


def update_keyboard_status():
    key = pygame.key.get_pressed()
    
def input_test(event):
    print(event.key)

if __name__ == '__main__':main() 


