#!/usr/bin/python


class Config:
    def __init__(self):
        pass

class DataBase:
    _layers = {}
    _conf = Config()

    def __init__(self):
        pass


    def load(file):
        if self._conf.check(file):
            self._conf.load(file)
            self._schema()



bdd = new DataBase()

bdd.load()
