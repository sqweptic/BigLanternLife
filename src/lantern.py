class _Lantern(object):
    ON = True
    OFF = False
    DEFAULT_COLOR = (255, 0, 0)
    
    def __init__(self):
        self._state = self.ON
        self._color = self.DEFAULT_COLOR
    
    def _draw(self):
        if self._state == self.ON:
            print('Lantern is ON and lighting {0}'.format(self._color))
        else:
            print('Lantern is OFF')
    
    def set_color(self, color):
        if isinstance(color, bytearray) and len(color) > 2:
            self._color = (color[0], color[1], color[2])
        self._draw()
        
    def is_on(self):
        return self._state == self.ON
    
    def on(self):
        self._state = self.ON
        self._draw()
        
    def off(self):
        self._state = self.OFF
        self._draw()
        
lantern_instance = _Lantern()
lantern_instance.on()

