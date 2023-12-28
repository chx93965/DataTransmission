import logging
from SX127x.LoRa import *

from service.StatsHandler import StatsHandler

logger1 = logging.getLogger("StatsTramsmitter")
logger1.setLevel(logging.DEBUG)
logger2 = logging.getLogger("LoRaTxImpl")
logger2.setLevel(logging.DEBUG)

# LoRa parameters
frequency = 915e6   # 915 MHz
verbose = True

class StatsTransmitter:

    def __init__(self):
        self.__stats_handler = StatsHandler()
        self.__lora = LoRaTxImpl(verbose)

    def transmit(self):
        pass


class LoRaTxImpl(LoRa):

    def __init__(self, verbose):
        super(LoRaTxImpl, self).__init__(verbose)
        self.set_mode(MODE.TX)

    def on_tx_done(self):
        logger2.info("TxDone")
        self.set_mode(MODE.SLEEP)