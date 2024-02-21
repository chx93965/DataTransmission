from source.common.helper import singleton
import logging
from machine import ADC, Pin

class DataReceiver(metaclass=singleton):

    def __init__(self):
        self.__pH_reader = ADC(Pin(25))
        self.__temperature_reader = ADC(Pin(26))
        self.__turbidity_reader = ADC(Pin(27))
        self.__pH = 0
        self.__temperature = 0
        self.__turbidity = 0
        self.__period = 1

    def read_data(self):
        self.__pH = self.__pH_reader.read_u16()
        self.__temperature = self.__temperature_reader.read_u16()
        self.__turbidity = self.__turbidity_reader.read_u16()

    def get_pH(self):
        return self.__pH

    def get_temperature(self):
        return self.__temperature

    def get_turbidity(self):
        return self.__turbidity

    def set_period(self, period):
        self.__period = period

    def get_period(self):
        return self.__period

    def __str__(self):
        return ("pH: " + str(self.__pH) +
                "\ntemperature: " + str(self.__temperature) +
                "\nturbidity: " + str(self.__turbidity) +
                "\nperiod: " + str(self.__period)) +\
                "\n"



