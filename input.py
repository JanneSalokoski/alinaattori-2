#!/usr/bin/env python

from logger import Logger

import csv
import sys


class Input:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def read(self):
        """Read a semicolon-delimitered csv input-file into a list"""
        self.logger.log("Reading input from file '{}'".format(self.config.input_file), start="\n")

        try:
            csv_reader = csv.DictReader(
                open(self.config.input_file, "r", encoding="utf-8-sig"),
                dialect="excel",
                delimiter=";"
            )

            data_rows = []
            for row in csv_reader:
                self.logger.log("Row: {}".format(row), Logger.LogLevel.DEBUG)
                data_rows.append(row)

            return data_rows

        except FileNotFoundError:
            self.logger.log(
                "No such file: '{}'".format(self.config.input_file),
                Logger.LogLevel.ERROR
            )
            sys.exit(1)

        except:  # noqa: E722
            print("Unexpected error", sys.exc_info()[0])
            raise Exception()
