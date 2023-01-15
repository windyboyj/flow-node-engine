import sys


class ExitNodeException(Exception):
    def __init__(self, code=500001, msg=""):
        self.code = code
        self.msg = msg

    def to_json(self):
        return {'code': self.code, 'msg': self.msg}


def display_exception():
    import traceback
    et, ev, tb = sys.exc_info()
    trace = traceback.format_exception(et, ev, tb, limit=1)
    msg = ''
    for _ in trace:
        msg += _.strip('\n') + ' '
    return msg


def get_logger(name="main"):
    import logging.handlers
    handler = logging.StreamHandler()
    log_format = logging.Formatter(fmt="%(asctime)s %(filename)s %(levelname)s %(message)s",
                                   datefmt="%Y/%m/%d %X")

    handler.setFormatter(log_format)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
