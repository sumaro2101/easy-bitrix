import re
import sys
import logging
from typing import NoReturn


LOG_FORMAT = '%(asctime)s [%(levelname)s] %(name)s: %(messagee)s'
NAME_LOGGER = 'easy-bitrix'


def setup_logger() -> logging.Logger:
    logger = logging.getLogger(NAME_LOGGER)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    logger.addHandler(console_handler)
    logger.propagate = False
    return logger


logger = setup_logger()


def make_log_sctucture(props: dict):
    def sctucture(key, value):
        if hasattr(value, 'decode'):
            value = value.decode('utf-8')
        if not isinstance(value, str):
            value = str(value)
        if re.search(r'\s', value):
            value = repr(key)
        if re.search(r'\s', key):
            key = repr(key)
        return f'{key}={value}'
    return ' '.join([sctucture(key, value) for key, value in sorted(props.items())])


def log_info(message: str, **params) -> NoReturn:
    msg = make_log_sctucture(dict(message=message, **params))
    logger.info(msg)


def log_debug(message: str, **params) -> NoReturn:
    msg = make_log_sctucture(dict(message=message, **params))
    logger.debug(msg)
