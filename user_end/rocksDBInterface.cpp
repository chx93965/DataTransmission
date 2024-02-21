#include "rocksDBInterface.h"
#include <iostream>

DBManager::DBManager(){
    this->dir = "./statsDB";
}

void DBManager::setDir(const char* dir){
    this->dir = dir;
}

char* DBManager::readValue(const char* key){
    try{
        std::string k(key);
        std::string v;
        rocksdb::Status status = db->Get(rocksdb::ReadOptions(), k, &v);
        char* value = new char[v.length() + 1];
        strcpy(value, v.c_str());
        return value;
    } catch (std::exception &e){
        throw e;
    }
}

void DBManager::writeValue(const char* key, const char* value){
    try{
        std::string k(key);
        std::string v(value);
        rocksdb::Status status = db->Put(rocksdb::WriteOptions(), k, v);
    } catch (std::exception &e){
        throw e;
    }
}

void DBManager::deleteValue(const char* key){
    try{
        std::string k(key);
        rocksdb::Status status = db->Delete(rocksdb::WriteOptions(), k);
    } catch (std::exception &e){
        throw e;
    }
}

void DBManager::openDB(){
    try{
        options.IncreaseParallelism();
        options.OptimizeLevelStyleCompaction();
        options.create_if_missing = true;
        rocksdb::Status status = rocksdb::DB::Open(options, dir, &db);
    } catch (std::exception &e){
        throw e;
    }
}

void DBManager::closeDB(){
    try{
        delete db;
    } catch (std::exception &e){
        throw e;
    }
}

int main(){}

