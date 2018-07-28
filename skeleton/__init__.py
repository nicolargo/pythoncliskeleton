#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Skeleton
#
# See AUTHORS file
# MIT Licence

# Import system libs
import signal

__appname__ = "Skeleton"
__version__ = "0.1"
__author__ = "Nicolas Hennion <nicolas@nicolargo.com>"
__licence__ = "MIT"

# Import others libs
from skeleton.main import SkeletonMain
from skeleton.logger import logger

# Add:
# from skeleton import <list of classes of the __all__ variable

def __signal_handler(signal, frame):
    """Callback for CTRL-C."""
    end()

def main():
    """Main entry point"""
    # Catch the CTRL-C signal
    signal.signal(signal.SIGINT, __signal_handler)

    # Init script
    core = SkeletonMain()
    args = core.args
