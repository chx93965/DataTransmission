import logging

from helper import synchronized, singleton
from StatsRegistry import StatsRegistry

logger = logging.getLogger("StatsHandler")
logger.setLevel(logging.DEBUG)

class StatsHandler(metaclass=singleton):

    def __init__(self):
        self.__stats_registry = StatsRegistry()

    @synchronized
    def get_stats(self):
        stats_list = []
        for stats in self.__stats_registry.get_registry().values():
            stats_list.append(stats)
        logger.debug("Requested: All stats")
        return stats_list

    @synchronized
    def get_stats_by_id(self, id):
        stats = self.__stats_registry.get(id)
        if stats is None:
            raise Exception("Stats #" + id + " does not exist")
        logger.debug("Requested: Stats #: " + id)
        return stats

    @synchronized
    def put_stats(self, stats_list):
        failures = []
        for stats in stats_list:
            id = stats.get_id()
            try:
                if self.__stats_registry.contains(id):
                    logger.debug("Updated: " + str(stats))
                else:
                    logger.debug("Created: " + str(stats))
                self.__stats_registry.put(stats)
            except Exception as e:
                failures.append(id)
                logger.error("Exception: " + str(e))

        if len(failures) > 0:
            raise Exception("Failed to update stats: " + str(failures))
        return failures

    @synchronized
    def delete_stats(self, id):
        stats = self.__stats_registry.get(id)
        if stats is None:
            logger.debug("Stats #" + id + " does not exist")
            raise Exception("Stats #" + id + " does not exist")
        self.__stats_registry.remove(id)
        logger.debug("Deleted: Stats #" + id)

    @synchronized
    def clear_stats(self):
        self.__stats_registry.clear()
        logger.debug("All stats cleared")