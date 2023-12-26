
class Stats:
    def __init__(self):
        self.__id = None
        self.__timestamp = None
        self.__pH = None
        self.__temperature = None
        self.__turbidity = None

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_timestamp(self):
        return self.__timestamp

    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp

    def get_pH(self):
        return self.__pH

    def set_pH(self, pH):
        self.__pH = pH

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_turbidity(self):
        return self.__turbidity

    def set_turbidity(self, turbidity):
        self.__turbidity = turbidity

    def equals(self, stats):
        return (self.__id == stats.get_id() and
                self.__timestamp == stats.get_timestamp() and
                self.__pH == stats.get_pH() and
                self.__temperature == stats.get_temperature() and
                self.__turbidity == stats.get_turbidity())

    def __str__(self):
        return ("id: " + str(self.__id) +
                "\ntimestamp: " + str(self.__timestamp) +
                "\npH: " + str(self.__pH) +
                "\ntemperature: " + str(self.__temperature) +
                "\nturbidity: " + str(self.__turbidity)) +\
                "\n"