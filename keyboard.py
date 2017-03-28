import pygame

class KeyHandler():
    
    def __init__(self):
        self.special_keys = []
        #self.message_event = message_event
        self.text = ""
        self.shift = False
        self.cursor_pos = 0
        self.actual_event = None
        #using to handle continuos pressing
        """self.start_tick_counter = 8000
        self.push_tick_counter = 2000
        self.pushed_down = False
        self.counter = 0
        """
        self.push_control = ButtonPushClock(8000,2000)

    def handle_key_up(self,event):
        if event.key == pygame.KMOD_LSHIFT or event.key == pygame.KMOD_RSHIFT:
            self.shift = False
        #elif event.key == self.actual_event.key:
        self.actual_event = None
        self.push_control.reset()

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
        self.actual_event = event
        print(self.cursor_pos)

    def _on_special_code(self,event):
        pass
        #self.message_event.put_msg(event) # I'll probably change this...add_event(event

    def move_cursor_r(self):
        self.cursor_pos = self.cursor_pos +1 if self.cursor_pos <= len(self.text) else len(self.text)

    def move_cursor_l(self):
        self.cursor_pos = max(self.cursor_pos -1, 0)

    def handle_on_clock(self):
        if self.actual_event is not None and self.push_control.tick():
            self.handle_key_down(self.actual_event)
            return True
        return False

class ButtonPushClock():
    
    def __init__(self,start_tick,push_tick):
        self.start_tick_max = start_tick
        self.push_tick_max = push_tick
        self.counter = 0
        self.push = False

    def _increase_counter(self):
        self.counter +=1

    def tick(self):
        self._increase_counter()
        self.push = self.push or (self.counter >= self.start_tick_max)
        if self.push and self.counter > self.push_tick_max:
            self.counter = 0
            return True
        return False

    def reset(self):
        self.counter = 0
        self.push = False
