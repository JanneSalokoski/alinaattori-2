#!/usr/bin/env python
#
# Here we should have some very toplevel documentation about Alinaattori 2.0
#

from enum import Enum


class Logger:
    """A logger class for easier output"""

    class LogLevel(Enum):
        SILENT = 0  # Completely silent operation
        ERROR = 1   # Only log errors
        LOG = 2     # Log all relevant info for standard usage
        DEBUG = 3   # Log everything, even debug info

    def __init__(self, loglevel):
        if isinstance(loglevel, self.LogLevel):
            self.loglevel = loglevel
        else:
            raise TypeError("loglevel must be of type Logger.LogLevel")

    def log(self, message, loglevel=LogLevel.LOG):
        if isinstance(loglevel, self.LogLevel):
            if loglevel.value <= self.loglevel.value:
                print("[{}]: {}".format(loglevel.name, message))

        else:
            raise TypeError("loglevel must be of type Logger.LogLevel")


def main():
    # Initialize Logger with a LogLevel
    # To-do: Get loglevel from user input
    logger = Logger(Logger.LogLevel.DEBUG);

    logger.log("Starting Alinaattori 2.0")


main()
