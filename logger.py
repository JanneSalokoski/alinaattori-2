#!/usr/bin/env python

from enum import Enum


class Logger:
    """A logger class for easier output"""

    class LogLevel(Enum):
        SILENT = 0  # Completely silent operation
        ERROR = 1   # Only log errors
        LOG = 2     # Log all relevant info for standard usage
        DEBUG = 3   # Log everything, even debug info

    def __init__(self, loglevel=LogLevel.LOG):
        self.loglevel = loglevel

    def log(self, message, loglevel=LogLevel.LOG, start="", end=""):
        if isinstance(loglevel, self.LogLevel):
            if loglevel.value <= self.loglevel.value:
                print("{}[{}] {}{}".format(start, loglevel.name, message, end))

        else:
            raise TypeError("loglevel must be of type Logger.LogLevel")
