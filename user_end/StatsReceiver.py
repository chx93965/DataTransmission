from DBManager import *
import logging
import socket
import json

logger = logging.getLogger("StatsReceiver")
logger.setLevel(logging.DEBUG)

# TODO: Move to config file
host = '0.0.0.0' # listen on all interfaces
port = 8080

class StatsReceiver(metaclass=singleton):

        def __init__(self):
            self.__db_manager = DBManager()
            self.__db_manager.set_db_dir(DBDir)
            self.__socket = None
            self.create_listen_socket()
            self.process_connections_forever()

        def create_listen_socket(self):
            try:
                self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.__socket.bind((host, port))
                self.__socket.listen(10)
                logger.info("Listening on " + host + ":" + str(port))
            except Exception as e:
                logger.error("Exception: " + str(e))

        def process_connections_forever(self):
            try:
                while True:
                    self.connection_handler(self.__socket.accept())
            except Exception as e:
                logger.error("Exception: " + str(e))
            finally:
                self.__socket.close()

        def connection_handler(self, client):
            socket, address = client
            logger.info("Connection received from {}".format(address))

            data_bytes = socket.recv(2048)
            data_decoded = data_bytes.decode('utf-8')
            stats = json.loads(data_decoded)
            logger.info("Received: " + str(stats))
            self.store_stats(stats)

        def store_stats(self, stats):
            key = stats['id']
            value = json.dumps(stats)
            self.__db_manager.write_value(key, value)

        def get_socket(self):
            return self.__socket

        def set_socket(self, socket):
            self.__socket = socket


if __name__ == '__main__':
    print("Listening on port {}...".format(port))
    stats_receiver = StatsReceiver()



