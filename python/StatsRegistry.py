
class StatsRegistry:
    def __init__(self):
        self.__registry = {}

    def put(self, stats):
        self.__registry[stats.get_id()] = stats

    def get(self, id):
        return self.__registry[id]

    def remove(self, id):
        del self.__registry[id]

    def replace(self, stats):
        self.__registry[stats.get_id()] = stats

    def contains(self, id):
        return id in self.__registry

    def clear(self):
        self.__registry.clear()

    def size(self):
        return len(self.__registry)

    def get_registry(self):
        return self.__registry

    def set_registry(self, registry):
        self.__registry = registry

    def __str__(self):
        output = "\nStatsRegistry{\n"
        for stats in self.__registry.values():
            output += str(stats) + "\n"
        output += "}"
        return output