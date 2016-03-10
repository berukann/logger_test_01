import logging

logger = logging.getLogger(__name__)

def test_fun():
  logger.debug("this is a debugging message in test_fun.")
  logger.info("this is an informational message in test_fun")
  logger.warn("this is a warning message in test_fun")
  logger.error("this is an error message in test_fun")
  logger.critical("this is a critical message in test_fun")
