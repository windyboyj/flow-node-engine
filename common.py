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
    size = 10 * 1024 * 1024
    handler = logging.handlers.RotatingFileHandler('app.log', 'a', size, 3)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
