import pygame

class KeyHandler():
    
    def __init__(self):
        self.special_keys = []
        #self.message_event = message_event
        self.text = ""
        self.shift = False
        self.cursor_pos = 0

    def handle_key_up(self,event):
        pass

    def handle_key_down(self,event):

        if event.key in self.special_keys:
            self._on_special_code(event)
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:self.cursor_pos-1] + self.text[self.cursor_pos+1:]
            self.move_cursor_l()
        elif event.key == pygame.K_RIGHT:
            self.move_cursor_r()

        elif event.key == pygame.K_LEFT:
            self.move_cursor_l()    
            
        elif event.key == pygame.KMOD_LSHIFT or event.key ==pygame.KMOD_RSHIFT:
            self.shift = True
        else:
            self.text = self.text[:self.cursor_pos] + chr(event.key) + self.text[self.cursor_pos:]
            self.move_cursor_r()

        print(self.cursor_pos)

    def _on_special_code(self,event):
        pass
        #self.message_event.put_msg(event) # I'll probably change this...add_event(event

    def move_cursor_r(self):
        self.cursor_pos = self.cursor_pos +1 if self.cursor_pos <= len(self.text) else len(self.text)

    def move_cursor_l(self):
        self.cursor_pos = max(self.cursor_pos -1, 0)
