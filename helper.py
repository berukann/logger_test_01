import logging
import os
import uuid
import coloredlogs


def init_logger_color():
    """ Initialize logger color using coloredlogs """
    if os.environ.get('COLOREDLOGS_LOG_LEVEL') is None:
        os.environ['COLOREDLOGS_LOG_LEVEL'] = 'INFO'
    if os.environ.get('COLOREDLOGS_LOG_FORMAT') is None:
        os.environ['COLOREDLOGS_LOG_FORMAT'] = '%(asctime)s [%(levelname)s] %(message)s'
    if os.environ.get('COLOREDLOGS_DATE_FORMAT') is None:
        os.environ['COLOREDLOGS_LOG_DATE_FORMAT'] = '%Y-%m-%d %H:%M:%S'
    coloredlogs.install()


def init_logger_file(out_dir, out_file):
    """ Initialize File Handler """
    # full path for output file
    full_path = os.path.join(out_dir, out_file)

    # Check to exist output directory
    if os.path.exists(out_dir):
        if os.path.exists(full_path):
            # If already exist out_file, rename out_file
            os.rename(full_path,
                      full_path + '.back.' + str(uuid.uuid4()))
    # Set File Handler
    logger = logging.getLogger()
    handler = logging.FileHandler(full_path, "w")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s (%(name)s) [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
