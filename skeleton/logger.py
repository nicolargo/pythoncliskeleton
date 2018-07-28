#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Skeleton
#
# See AUTHORS file
# MIT Licence

"""Custom logger class."""

import os
import json
import getpass
import tempfile

import logging
import logging.config

LOG_FILENAME = os.path.join(tempfile.gettempdir(),
                            'skeleton-{}.log'.format(getpass.getuser()))

# Define the logging configuration
LOGGING_CFG = {
    "version": 1,
    "disable_existing_loggers": "False",
    "root": {
        "level": "INFO",
        # "handlers": ["file", "console"]
        "handlers": ["console"]
    },
    "formatters": {
        "standard": {
            "format": "%(asctime)s -- %(levelname)s -- %(message)s"
        },
        "short": {
            "format": "%(levelname)s -- %(message)s"
        },
        "long": {
            "format": "%(asctime)s -- %(levelname)s -- %(message)s (%(funcName)s in %(filename)s)"
        },
        "free": {
            "format": "%(message)s"
        }
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "filename": LOG_FILENAME
        },
        "console": {
            "level": "CRITICAL",
            "class": "logging.StreamHandler",
            "formatter": "free"
        }
    },
    "loggers": {
        "debug": {
            # "handlers": ["file", "console"],
            "handlers": ["console"],
            "level": "DEBUG"
        },
        "verbose": {
            # "handlers": ["file", "console"],
            "handlers": ["console"],
            "level": "INFO"
        },
        "standard": {
            "handlers": ["console"],
            "level": "INFO"
        },
    }
}


def _main_logger(env_key='LOG_CFG'):
    """Build and return the logger.

    env_key define the env var where a path to a specific JSON logger
            could be defined

    :return: logger -- Logger instance
    """
    _logger = logging.getLogger()

    # By default, use the LOGGING_CFG logger configuration
    config = LOGGING_CFG

    # Check if a specific configuration is available
    user_file = os.getenv(env_key, None)
    if user_file and os.path.exists(user_file):
        # A user file as been defined. Use it...
        with open(user_file, 'rt') as f:
            config = json.load(f)

    # Load the configuration
    logging.config.dictConfig(config)

    return _logger


logger = _main_logger()
