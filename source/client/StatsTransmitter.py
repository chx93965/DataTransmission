import logging
import socket

from source.service.StatsHandler import StatsHandler

logger = logging.getLogger("StatsTramsmitter")
logger.setLevel(logging.DEBUG)

# TODO: Move to config file
server = '127.0.0.1'  # server IP
port = 8080

class StatsTransmitter:

    def __init__(self):
        self.__socket = None
        self.__stats_handler = StatsHandler()
        self.create_socket()
        self.connect_to_server()

    def create_socket(self):
        try:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            logger.error("Exception: " + str(e))

    def connect_to_server(self):
        try:
            self.__socket.connect((server, port))
        except Exception as e:
            logger.error("Exception: " + str(e))

    def transmit(self):
        try:
            stats = self.__stats_handler.pop_stats(id)
            logger.info("Transmitting: " + str(stats))
            self.__socket.sendall(str(stats).encode('utf-8'))
        except Exception as e:
            logger.error("Exception: " + str(e))

    def shutdown(self):
        try:
            self.__socket.close()
            logger.info("Shutdown")
        except Exception as e:
            logger.error("Exception: " + str(e))



