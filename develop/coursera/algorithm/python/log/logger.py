import os, sys
import logging
import traceback

class Logger(object):
    _logger = logging.getLogger('mylogger')
    _logger.setLevel(logging.DEBUG)

    # _log_file = _cfg.get_log_file()
    # _log_dir = os.path.dirname(_log_file)

    # # clean & recreate log file
    # if os.path.exists(_log_file):
    #     os.remove(_log_file)
    # if not os.path.isdir(_log_dir):
    #     os.makedirs(_log_dir)
    # open(_log_file, 'w').close()

    # file log handler
    # _fh = logging.FileHandler(_log_file)
    # _fh.setLevel(logging.INFO)

    # console log handler
    _sh = logging.StreamHandler()
    _sh.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    # _fh.setFormatter(formatter)
    _sh.setFormatter(formatter)

    # _logger.addHandler(_fh)
    _logger.addHandler(_sh)

    @staticmethod
    def debug(message):
        Logger._logger.debug(message)

    @staticmethod
    def info(message):
        Logger._logger.info(message)

    @staticmethod
    def warn(message):
        Logger._logger.warn(message)

    @staticmethod
    def error(message):
        Logger._logger.error(message)

    @staticmethod
    def exception(message = None):
        if message:
            try:
                Logger.error(message + '\n' + traceback.format_exc())
            except:
                Logger.error(message)
        else:
            try:
                Logger.error(traceback.format_exc())
            except:
                Logger.error('error')