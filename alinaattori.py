#!/usr/bin/env python
#
# Here we should have some very toplevel documentation about Alinaattori 2.0
#

from enum import Enum

import csv
import sys


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
    """Read a semicolon-delimitered csv input-file into a list"""
    logger.log("Reading input from file '{}'".format(input_file))

    try:
        csv_reader = csv.DictReader(
            open(input_file, "r", encoding="utf-8-sig"),
            dialect="excel",
            delimiter=";"
        )

        data_rows = []
        for row in csv_reader:
            data_rows.append(row)

        logger.log("data_rows: {}".format(data_rows), Logger.LogLevel.DEBUG)

    except FileNotFoundError:
        logger.log(
            "No such file: '{}'".format(input_file),
            Logger.LogLevel.ERROR
        )
        sys.exit(1)

    except:  # noqa: E722
        print("Unexpected error", sys.exc_info()[0])
        raise()


def main():
    # Initialize Config
    # To-do: Get these from user input
    config = Config("input.csv", "output.csv", Logger.LogLevel.DEBUG)

    # Initialize Logger with a LogLevel
    logger.loglevel = config.loglevel

    logger.log("Starting Alinaattori 2.0")

    request_data = read_input(config.input_file)

    logger.log(request_data, Logger.LogLevel.DEBUG)


main()
