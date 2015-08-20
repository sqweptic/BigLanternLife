import struct

import tornado.ioloop

from lantern import lantern_instance

class LanternConnector(object):
    LANTERN_COMMANDS = {
        0x12: 'on',
        0x13: 'off',
        0x20: 'set_color'
    }
    
    def __init__(self, stream_future):
        if stream_future.done() and stream_future.exception() is None:
            self.stream = stream_future.result()
            self.process()
#         else:
#             there is no exception handling
            
    def process(self):
        self.stream.read_until_close(callback = self.receive_raw_data)
    
    def close(self):
        self.stream.close()
        tornado.ioloop.IOLoop.current().stop()
        
    def receive_raw_data(self, data):
        print('new command from server')
        value_len = len(data) - 3
        command, length, raw_value = struct.unpack('>BH' + str(value_len) + 's', 
                                                   data)
        
        value = bytearray(raw_value[:length])
        
        self.apply_command(command, length, value)
        
        self.close()
        
    def apply_command(self, command, length, value):
        if command in self.LANTERN_COMMANDS:
            lantern_method = getattr(lantern_instance, 
                                     self.LANTERN_COMMANDS[command])
            if length and value:
                lantern_method(value)
            else:
                lantern_method()
        

