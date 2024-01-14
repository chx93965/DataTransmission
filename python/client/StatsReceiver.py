import logging
import socket
import time

# from SX127x.LoRa import *
# from SX127x.board_config import BOARD

logger = logging.getLogger("StatsReceiver")
logger.setLevel(logging.DEBUG)
# logger2 = logging.getLogger("LoRaRxImpl")
# logger2.setLevel(logging.DEBUG)

# # LoRa parameters
# frequency = 915e6   # 915 MHz
# verbose = True
# TODO: Move to config file
host = '0.0.0.0' # listen on all interfaces
port = 8080

class StatsReceiver:

        def __init__(self):
            # self.__lora = LoRaRxImpl(verbose)
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket.bind((host, port))
            # start listening for connections
            self.__socket.listen(1)
            logger.info("Listening on " + host + ":" + str(port))

        def receive(self):
            while True:
                client, address = self.__socket.accept()
                logger.info("Connection from " + str(address))
                request = client.recv(1024)
                stats = request.decode('utf-8')
                logger.info("Received: " + stats)
                self.store_stats(stats)
                client.close()

        def store_stats(self, stats):
            pass

        def get_socket(self):
            return self.__socket

        def set_socket(self, socket):
            self.__socket = socket

# class LoRaRxImpl(LoRa):
#
#     def __init__(self, verbose):
#         super(LoRaRxImpl, self).__init__(verbose)
#         self.set_mode(MODE.SLEEP)
#
#     def on_rx_done(self):
#         logger2.info("RxDone")
#         self.set_mode(MODE.SLEEP)
#         self.reset_ptr_rx()
#         self.set_mode(MODE.RXCONT)
#
#     def on_rx_timeout(self):
#         logger2.info("RxTimeout")
