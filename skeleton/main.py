#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Skeleton
#
# See AUTHORS file
# MIT Licence

# Import libs
import argparse
import logging
import sys

# Global variables
__appname__ = "Skeleton"
__version__ = "0.1"
__author__ = "Nicolas Hennion <nicolas@nicolargo.com>"
__licence__ = "MIT"

# Configure logger
logging.basicConfig(format='%(asctime)-15s %(message)s')
logger = logging.getLogger(__appname__)


class SkeletonMain(object):
    """Main class to manage instance."""

    # Version
    version = "{} {}".format(__appname__, __version__)
    # version = "".format()

    # Examples of use
    example_of_use = """
Examples of use: ...
"""

    def __init__(self):
        """Manage the command line arguments."""
        # Read the command line arguments
        self.args = self.parse_args()

    def parse_args(self):
        """Parse command line arguments."""
        # Manage args
        parser = argparse.ArgumentParser(
            prog='__appname__',
            conflict_handler='resolve',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=self.example_of_use)

        parser.add_argument('-V', '--version', action='version',
                            version=self.version)
        parser.add_argument('-d', '--debug', action='store_true', default=False,
                            dest='debug', help='enable debug mode')

        args = parser.parse_args()

        # Debug mode
        if args.debug:
            from logging import DEBUG
            logger.setLevel(DEBUG)
            logger.debug("Debug mode is ON")
        else:
            from warnings import simplefilter
            simplefilter("ignore")

        return args
