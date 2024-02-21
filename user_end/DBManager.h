#ifndef DBMANAGER_H
#define DBMANAGER_H

#include <string>
#include "rocksdb/db.h"
#include "rocksdb/options.h"

class DBManager{
    public:
        rocksdb::DB* db;
        rocksdb::Options options;
        std::string dir;
        DBManager();
        void setDir(const char* dir);
        char* readValue(const char* key);
        void writeValue(const char* key, const char* value);
        void deleteValue(const char* key);
        void openDB();
        void closeDB();
};

// Declare C-linkage functions
#ifdef __cplusplus
extern "C" {
#endif
    DBManager* DBManager_new(){ return new DBManager(); }
    void DBManager_setDir(DBManager* dbm, const char* dir){ dbm->setDir(dir); }
    char* DBManager_readValue(DBManager* dbm, const char* key){ return dbm->readValue(key); }
    void DBManager_writeValue(DBManager* dbm, const char* key, const char* value){ dbm->writeValue(key, value); }
    void DBManager_deleteValue(DBManager* dbm, const char* key){ dbm->deleteValue(key); }
    void DBManager_openDB(DBManager* dbm){ dbm->openDB(); }
    void DBManager_closeDB(DBManager* dbm){ dbm->closeDB(); }
#ifdef __cplusplus
}
#endif

#endif // DBMANAGER_H