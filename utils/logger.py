import logging


def setup_logger():
    logger = logging.getLogger('app_ui_icon_test')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(快照 of the current state of the app)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger