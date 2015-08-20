import socket

import tornado.ioloop
from tornado.tcpclient import TCPClient

from lantern_connector import LanternConnector     


HOST = '127.0.0.1'
PORT = 9999

def get_connection_data():
    _host = input('host(127.0.0.1): ')
    if not _host:
        _host = HOST
    _port = input('port(9999): ')
    if not _port:
        _port = PORT
    return (_host, _port)

def main():
    host, port = get_connection_data()
    stream_future = TCPClient().connect(host=host, port=port, af=socket.AF_INET)
    tornado.ioloop.IOLoop.current().add_future(stream_future, LanternConnector)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
    