#!/usr/bin/env python
#
# Here we should have some very toplevel documentation about Alinaattori 2.0
#

from enum import Enum


class Config:
    """Create a data-structure for handling configuration"""

    def __init__(self, input_file, output_file, loglevel):
        self.input_file = input_file
        self.output_file = output_file
        self.loglevel = loglevel


class Logger:
    """A logger class for easier output"""

    class LogLevel(Enum):
        SILENT = 0  # Completely silent operation
        ERROR = 1   # Only log errors
        LOG = 2     # Log all relevant info for standard usage
        DEBUG = 3   # Log everything, even debug info

    def __init__(self):
        self._loglevel = self.LogLevel.DEBUG

    @property
    def loglevel(self):
        return self._loglevel

    @loglevel.setter
    def loglevel(self, loglevel):
        if isinstance(loglevel, self.LogLevel):
            self._loglevel = loglevel
        else:
            raise TypeError("loglevel must be of type Logger.LogLevel")

    def log(self, message, loglevel=LogLevel.LOG):
        if isinstance(loglevel, self.LogLevel):
            if loglevel.value <= self.loglevel.value:
                print("[{}]: {}".format(loglevel.name, message))

        else:
            raise TypeError("loglevel must be of type Logger.LogLevel")


# Initialize global Logger-class
logger = Logger()


def read_input(input_file):
    logger.log("Testi")


def main():
    # Initialize Config
    # To-do: Get these from user input
    config = Config("input.csv", "output.csv", Logger.LogLevel.DEBUG)

    # Initialize Logger with a LogLevel
    logger.loglevel = config.loglevel

    logger.log("Starting Alinaattori 2.0")

    request_data = read_input(config.input_file)


main()
