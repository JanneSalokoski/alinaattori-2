#!/usr/bin/env python

from lib.logger import Logger

import random


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


class Requests:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def process_raw_request_data(self, data):
        """Parse raw request data into a list of Request objects"""
        self.logger.log("Processing raw request data", start="\n")
        requests = []

        for row in data:
            request = Request(
                row["organization"],
                row["email"],
                [row["1"], row["2"], row["3"]]
            )

            self.logger.log("Request: {}"
                .format(request), Logger.LogLevel.DEBUG  # noqa: E128
            )
            requests.append(request)

        return requests

    def validate_date(self, date, reservations):
        """Check if date is found in reserved_dates"""
        for reservation in reservations:
            self.logger.log("{} == {} -> {}".format(
                date,
                reservation.date,
                date == reservation.date
            ), Logger.LogLevel.DEBUG)

            if date == reservation.date:
                return False

        return True

    def randomize_requests(self, requests):
        """Randomize requests list"""
        self.logger.log("Randomizing request order", start="\n")
        random.shuffle(requests)

    def process_request(self, request, reservations):
        """Validate all dates of a request"""
        self.logger.log(
            "Processing organization '{}'".format(request.organization),
            Logger.LogLevel.DEBUG,
            start="\n"
        )
        for date in request.dates:
            if self.validate_date(date, reservations):
                self.logger.log("Reserved date '{}' for organization '{}'"
                    .format(  # noqa: E128
                        date,
                        request.organization
                    )
                )
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
            "1.1.1970"
        )

    def process_requests(self, requests):
        """Validate requests and return reservations"""
        self.logger.log("Processing requests", start="\n")

        self.randomize_requests(requests)

        reservations = []
        for request in requests:
            reservations.append(self.process_request(request, reservations))

        return reservations
