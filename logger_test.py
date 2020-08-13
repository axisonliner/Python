import os
import logging


def user_name():
    us_name = os.uname()
    if us_name[0] == 'Darwin':
        return "MacOS:" + us_name[1].replace(".local", "")
    else:
        return "PC:" + us_name[1].replace(".local", "")


LOG_FORMAT = "%(levelname)s " \
             "%(asctime)s " \
             "{0} " \
             "funcName:%(funcName)s " \
             "line:%(lineno)d " \
             "%(message)s".format(user_name())
logging.basicConfig(filename="log_file.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT)
                    # filemode="w")

# logger.info("Test message")
# print(logger.level)
# logger.info('simple message')


logger = logging.getLogger()


def division(a, b):
    # logger.info("func values: ({0}, {1})".format(a, b))
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        logger.exception('func values: {0} / {1}'.format(a, b))
        # logger.warning(sys.exc_info()[0])


division(5, 0)
# logger.warning(division(5, 0))
# logger.critical('critical message')
