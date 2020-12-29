import logging


class Logger(object):
    def __init__(self, name="__name__"):
        self.name = name
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(self.handler)
        return logger

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def info(self, msg):
        self.logger.info(msg)


class BotLogger(Logger):
    def __init__(self, username):
        super().__init__()
        self.name = username
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - {}: %(message)s'.format(username))
        self.handler.setFormatter(self.formatter)
