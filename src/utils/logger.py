import logging

custom_logger = logging.getLogger("logger")


class Logger:
    """
    Custom logger class
    """

    @staticmethod
    def debug(message):
        custom_logger.debug(message)

    @staticmethod
    def info(message):
        custom_logger.info(message)

    @staticmethod
    def warning(message):
        custom_logger.warning(message)

    @staticmethod
    def error(message):
        custom_logger.error(message)

    @staticmethod
    def critical(message):
        custom_logger.critical(message)


logger = Logger()
