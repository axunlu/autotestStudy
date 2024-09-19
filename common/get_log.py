import sys
import logging.config
import logging


def get_log():
    con_log = "../configs/log.conf"
    logging.config.fileConfig(con_log)
    log = logging.getLogger()
    return log
