import socket

import tornado.ioloop
from tornado.tcpclient import TCPClient

from lantern_connector import LanternConnector     


def get_connection_data():
    return ('127.0.0.1', 9999)

def main():
    host, port = get_connection_data()
    stream_future = TCPClient().connect(host=host, port=port, af=socket.AF_INET)
    tornado.ioloop.IOLoop.current().add_future(stream_future, LanternConnector)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
    