import struct

import tornado.ioloop

from lantern import lantern_instance

class LanternConnector(object):
    def __init__(self, stream_future):
        if stream_future.done() and stream_future.exception() is None:
            self.stream = stream_future.result()
            self.process()
            
    def process(self):
        self.stream.read_until_close(callback = self.receive_raw_data)
    
    def close(self):
        self.stream.close()
        tornado.ioloop.IOLoop.current().stop()
        
    def receive_raw_data(self, data):
        print('data get')
        value_len = len(data) - 3
        command, length, raw_value = struct.unpack('>BH' + str(value_len) + 's', 
                                                   data)
        
        value = raw_value[:length]
        
        print(command, length, len(value))
        
        self.close()
        

