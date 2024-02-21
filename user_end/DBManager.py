from common.helper import singleton
from ctypes import cdll
from ctypes import c_char_p
import logging

logger = logging.getLogger("DBManager")
logger.setLevel(logging.DEBUG)

lib = cdll.LoadLibrary('./DBManager.so')
DBDir = "../statsDB"
lib.DBManager_readValue.restype = c_char_p

class DBManager(metaclass=singleton):
    def __init__(self):
        self.obj = lib.DBManager_new()

    def set_db_dir(self, dir):
        dir = dir.encode('utf-8')
        lib.DBManager_setDir(self.obj, dir)

    def read_value(self, key):
        try:
            key = key.encode('utf-8')
            return lib.DBManager_readValue(self.obj, key)
        except Exception as e:
            logger.error("Exception: " + str(e))

    def write_value(self, key, value):
        try:
            key = key.encode('utf-8')
            value = value.encode('utf-8')
            lib.DBManager_writeValue(self.obj, key, value)
        except Exception as e:
            logger.error("Exception: " + str(e))

    def delete_value(self, key):
        try:
            key = key.encode('utf-8')
            lib.DBManager_deleteValue(self.obj, key)
        except Exception as e:
            logger.error("Exception: " + str(e))

    def open_db(self):
        try:
            lib.DBManager_openDB(self.obj)
        except Exception as e:
            logger.error("Exception: " + str(e))
    def close_db(self):
        try:
            lib.DBManager_closeDB(self.obj)
        except Exception as e:
            logger.error("Exception: " + str(e))
