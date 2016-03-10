from logging import getLogger
from test import test_fun

from helper import init_logger_color, init_logger_file

init_logger_color()
init_logger_file('/Users/daicho/Work/201603/Python', 'vm_import_debug.log')
logger = getLogger(__name__)


def main():
    print("Main Thread")
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warn("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")
    print("Test Func Thread")
    test_fun()

if __name__ == '__main__':
    main()
