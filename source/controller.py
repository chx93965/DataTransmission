import logging
import time

from common.helper import ControllerState
from common.Stats import *
from service.StatsHandler import *
from client.StatsTransmitter import *
from client.DataReceiver import *

logger = logging.getLogger("Controller")
logger.setLevel(logging.DEBUG)

class Controller:

    def __init__(self):
        self.__state = ControllerState.IDLE
        self.__current_id = 0
        self.__data_receiver = DataReceiver()
        self.__stats_handler = StatsHandler()
        self.__stats_transmitter = StatsTransmitter()

    def capture(self):
        self.__state = ControllerState.BUSY
        pH = self.__data_receiver.get_pH()
        temperature = self.__data_receiver.get_temperature()
        turbidity = self.__data_receiver.get_turbidity()
        stats = Stats()
        stats.set_id(self.__current_id)
        stats.set_pH(pH)
        stats.set_temperature(temperature)
        stats.set_turbidity(turbidity)
        stats.set_timestamp(time.time())
        self.cache(stats)

    def cache(self, stats):
        self.__stats_handler.push_stats(stats)
        self.__current_id += 1
        self.transmit()

    def transmit(self):
        self.__state = ControllerState.IDLE
        self.__stats_transmitter.transmit()

    def on_error(self):
        self.__state = ControllerState.ERROR

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def get_current_id(self):
        return self.__current_id


if __name__ == '__main__':
    print("Hello World!")
    controller = Controller()
    while True:
        controller.capture()
        time.sleep(1)