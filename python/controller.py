import logging
from common.helper import ControllerState
import itertools

logger = logging.getLogger("Controller")
logger.setLevel(logging.DEBUG)
count = itertools.count(start=-1, step=1)

class Controller:

    def __init__(self):
        self.__state = ControllerState.IDLE
        self.__current_id = next(count)

    def on_receive(self):
        if self.__state == ControllerState.BUSY:
            return False
        state = ControllerState.BUSY
        self.on_transmit()
        return True

    def on_transmit(self):
        self.__state = ControllerState.IDLE

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