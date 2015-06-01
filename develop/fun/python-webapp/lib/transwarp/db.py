#! /usr/bin/env ptyhon
import threading 

class _Engine(object):
    def __init__(self, connect):
        self.connect = connect

    def connect(self):
        return self.connect()

class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transatctions = 0

    def is_init(self):
        return not self.connect is None

    def init(self):
        self.connection =  _LasyConnntion()
        self.transactions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

    def cursor(self):
        return self.connection.cursor()

_db_ctx = _DbCtx()

class _ConnectionCtx(object):
    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self

    def __exit__(self, exctype, excvalue, traceback):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()

def connection():
    return _ConnectionCtx()

