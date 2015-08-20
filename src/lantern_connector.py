from lantern import lantern_instance

class LanternConnector(object):
    def __init__(self, stream_future):
        if stream_future.done() and stream_future.exception() is None:
            self.set_connection(stream_future.result())
            self.process()
            
    def set_connection(self, stream):
        self.stream = stream
    
    def process(self):
        print('process connection')
        