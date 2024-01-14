import logging
import socket

from SX127x.LoRa import *

from service.StatsHandler import StatsHandler

logger = logging.getLogger("StatsTramsmitter")
logger.setLevel(logging.DEBUG)
# logger2 = logging.getLogger("LoRaTxImpl")
# logger2.setLevel(logging.DEBUG)

# # LoRa parameters
# frequency = 915e6   # 915 MHz
# verbose = True
# TODO: Move to config file
server = '127.0.0.1' # server IP
port = 8080

class StatsTransmitter:

    def __init__(self):
        # self.__lora = LoRaTxImpl(verbose)
        self.__stats_handler = StatsHandler()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to server
        self.__socket.connect((server, port))

    def transmit(self, id):
        stats = self.__stats_handler.pop_stats(id)
        logger.info("Transmitting: " + str(stats))
        self.__socket.sendall(str(stats).encode('utf-8'))
        self.__socket.close()

    def get_socket(self):
        return self.__socket

    def set_socket(self, socket):
        self.__socket = socket


# class LoRaTxImpl(LoRa):
#
#     def __init__(self, verbose):
#         super(LoRaTxImpl, self).__init__(verbose)
#         self.set_mode(MODE.TX)
#
#     def on_tx_done(self):
#         logger2.info("TxDone")
#         self.set_mode(MODE.SLEEP)