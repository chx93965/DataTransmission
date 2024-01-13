import logging
from common.helper import ControllerState

logger = logging.getLogger("Controller")
logger.setLevel(logging.DEBUG)

class Controller:

    def __init__(self):
        state = ControllerState.IDLE

    def on_receive(self):
        if self.state == ControllerState.BUSY:
            return False
        state = ControllerState.BUSY
        self.on_transmit()
        return True

    def on_transmit(self):
        self.state = ControllerState.IDLE

    def on_error(self):
        self.state = ControllerState.ERROR

if __name__ == '__main__':
    print("Hello World!")