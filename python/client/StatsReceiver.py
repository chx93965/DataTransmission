import logging
from SX127x.LoRa import *
from SX127x.board_config import BOARD

logger2 = logging.getLogger("LoRaRxImpl")
logger2.setLevel(logging.DEBUG)

# LoRa parameters
frequency = 915e6   # 915 MHz
verbose = True

class StatsReceiver:

        def __init__(self):
            self.__lora = LoRaRxImpl(verbose)

        def receive(self):
            pass

class LoRaRxImpl(LoRa):

    def __init__(self, verbose):
        super(LoRaRxImpl, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)

    def on_rx_done(self):
        logger2.info("RxDone")
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_rx_timeout(self):
        logger2.info("RxTimeout")
