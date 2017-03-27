import pygame

class KeyHandler():
    
    def __init__(self):
        self.special_keys = []
        #self.message_event = message_event
        self.text = ""
        self.shift = False
        self.cursor_pos = -1

    def handle_key_up(self,event):
        pass

    def handle_key_down(self,event):
        if event.key in self.special_keys:
            self._on_special_code(event)
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:self.cursor_pos] + self.text[self.cursor_pos+1:]
            self.cursor_pos-=1
        elif event.key == pygame.K_RIGHT:
            self.cursor_pos = min(self.cursor_pos+1,len(self.text))
        elif event.key == pygame.K_LEFT:
            self.cursor_pos = max(0,self.cursor_pos-1)
        elif event.key == pygame.KMOD_LSHIFT or event.key ==pygame.KMOD_RSHIFT:
            self.shift = True
        else:
            print(":")
            self.text = self.text[:self.cursor_pos] + chr(event.key) + self.text[self.cursor_pos:]
            self.cursor_pos+=1
            print(chr(event.key))
    
    def _on_special_code(self,event):
        print("log therapy")
        #self.message_event.put_msg(event) # I'll probably change this...add_event(event


