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


class Request:
    """Create a data-structure for handling requests"""

    def __init__(self, organization, email, dates):
        self.organization = organization
        self.email = email
        self.dates = dates

    def __repr__(self):
        return "organization: '{}', email: '{}', dates: '{}'".format(
            self.organization,
            self.email,
            self.dates
        )


class Reservation:
    """Create a data-structure for handling reservations"""

    def __init__(self, organization, status, email, date):
        self.organization = organization
        self.status = status
        self.email = email
        self.date = date

    def __repr__(self):
        return ("organization: '{}', status: '{}' " +
                "email: '{}', date: '{}'").format(
                    self.organization,
                    "Ok" if self.status is True else "Failed",
                    self.email,
                    self.date
                )


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
        return data_rows

    except FileNotFoundError:
        logger.log(
            "No such file: '{}'".format(input_file),
            Logger.LogLevel.ERROR
        )
        sys.exit(1)

    except:  # noqa: E722
        print("Unexpected error", sys.exc_info()[0])
        raise()


def process_raw_request_data(data):
    """Parse raw request data into a list of Request objects"""
    requests = []

    for row in data:
        requests.append(Request(
            row["organization"],
            row["email"],
            [row["1"], row["2"], row["3"]]
        ))

    logger.log("Requests: {}".format(requests), Logger.LogLevel.DEBUG)
    return requests


def validate_date(date, reservations):
    """Check if date is found in reserved_dates"""
    for reservation in reservations:
        logger.log("{} == {} -> {}".format(
            date,
            reservation.date,
            date == reservation.date
        ), Logger.LogLevel.DEBUG)

        if date == reservation.date:
            return False

    return True


def process_request(request, reservations):
    """Validate all dates of a request"""
    for date in request.dates:
        if validate_date(date, reservations):
            return Reservation(
                request.organization,
                True,
                request.email,
                date
            )

    return Reservation(
        request.organization,
        False,
        request.email,
        0
    )


def process_requests(requests):
    """Validate requests and return reservations"""
    reservations = []
    for request in requests:
        reservations.append(process_request(request, reservations))

    logger.log("Reservations: {}".format(reservations), Logger.LogLevel.DEBUG)
    return reservations


def main():
    # Initialize Config
    # To-do: Get these from user input
    config = Config("input.csv", "output.csv", Logger.LogLevel.DEBUG)

    # Initialize Logger with a LogLevel
    logger.loglevel = config.loglevel

    logger.log("Starting Alinaattori 2.0")

    raw_request_data = read_input(config.input_file)
    requests = process_raw_request_data(raw_request_data)

    reservations = process_requests(requests)


main()
