#!/usr/bin/env python
#
# Here we should have some very toplevel documentation about Alinaattori 2.0
#

from enum import Enum

import random
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

    def log(self, message, loglevel=LogLevel.LOG, start="", end=""):
        if isinstance(loglevel, self.LogLevel):
            if loglevel.value <= self.loglevel.value:
                print("{}[{}] {}{}".format(start, loglevel.name, message, end))

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
    logger.log("Reading input from file '{}'".format(input_file), start="\n")

    try:
        csv_reader = csv.DictReader(
            open(input_file, "r", encoding="utf-8-sig"),
            dialect="excel",
            delimiter=";"
        )

        data_rows = []
        for row in csv_reader:
            logger.log("Row: {}".format(row), Logger.LogLevel.DEBUG)
            data_rows.append(row)

        return data_rows

    except FileNotFoundError:
        logger.log(
            "No such file: '{}'".format(input_file),
            Logger.LogLevel.ERROR
        )
        sys.exit(1)

    except:  # noqa: E722
        print("Unexpected error", sys.exc_info()[0])
        raise Exception()


def process_raw_request_data(data):
    """Parse raw request data into a list of Request objects"""
    logger.log("Processing raw request data", start="\n")
    requests = []

    for row in data:
        request = Request(
            row["organization"],
            row["email"],
            [row["1"], row["2"], row["3"]]
        )

        logger.log("Request: {}".format(request), Logger.LogLevel.DEBUG)
        requests.append(request)

    #logger.log("Requests: {}".format(requests), Logger.LogLevel.DEBUG)
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


def randomize_requests(requests):
    """Randomize requests list"""
    logger.log("Randomizing request order", start="\n")
    random.shuffle(requests)


def process_request(request, reservations):
    """Validate all dates of a request"""
    logger.log(
        "Processing organization '{}'".format(request.organization),
        Logger.LogLevel.DEBUG,
        start="\n"
    )
    for date in request.dates:
        if validate_date(date, reservations):
            logger.log("Reserved date '{}' for organization '{}'".format(
                date,
                request.organization
            ))
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
        "0"
    )


def process_requests(requests):
    """Validate requests and return reservations"""
    logger.log("Processing requests", start="\n")
    reservations = []
    for request in requests:
        reservations.append(process_request(request, reservations))

    #logger.log("Reservations: {}".format(reservations), Logger.LogLevel.DEBUG)
    return reservations


def print_stdout(reservations):
    """Print output to stdout"""
    logger.log("Reservations: ", start="\n")

    for reservation in reservations:
        logger.log("'{}': '{}'".format(
            reservation.organization,
            reservation.date
        ))


def print_file(reservations, config):
    """Print succesfull reservations and failures into output file"""
    logger.log(
        "Printing output to file '{}'".format(config.output_file),
        start="\n"
    )

    try:
        with open(config.output_file, "w", newline="", encoding="utf-8-sig") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=";", dialect="excel")
            csvwriter.writerow(["organization", "success", "date"])
            for reservation in reservations:
                csvwriter.writerow([
                    reservation.organization,
                    reservation.status,
                    reservation.date
                ])

        csvfile.close()

    except IOError:
        logger.log(
            "Can't open file: '{}'".format(config.output_file),
            Logger.LogLevel.ERROR
        )
        sys.exit(1)

    except:  # noqa: E722
        print("Unexpected error", sys.exc_info()[0])
        raise Exception()


def output_reservations(reservations, config):
    """Print output to stdout and to the output file"""
    print_stdout(reservations)
    print_file(reservations, config)


def main():
    # Initialize Config
    # To-do: Get these from user input
    config = Config("input.csv", "output.csv", Logger.LogLevel.LOG)

    # Initialize Logger with a LogLevel
    logger.loglevel = config.loglevel

    logger.log("Starting Alinaattori 2.0", start="\n")

    raw_request_data = read_input(config.input_file)
    requests = process_raw_request_data(raw_request_data)

    randomize_requests(requests)

    reservations = process_requests(requests)

    output_reservations(reservations, config)

    logger.log("Program finished succesfully", start="\n", end="\n")


main()
