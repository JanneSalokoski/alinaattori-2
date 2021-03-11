#!/usr/bin/env python

from lib.logger import Logger

from datetime import datetime

import csv
import sys


class Output:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def sort(self, reservations):
        """Sort reservations alphabetically"""
        return sorted(reservations, key=lambda i: i.organization)

    def stdout(self, reservations):
        """Print output to stdout"""
        self.logger.log("Reservations: ", start="\n")

        for reservation in self.sort(reservations):
            self.logger.log("'{}': '{}' -> {}".format(
                reservation.organization,
                reservation.date,
                reservation.status
            ))

    def file(self, reservations):
        """Print succesfull reservations and failures into output file"""
        self.logger.log(
            "Printing output to file '{}'".format(self.config.output_file),
            start="\n"
        )

        try:
            with open(
                self.config.output_file,
                    "w",
                    newline="",
                    encoding="utf-8-sig"
                    ) as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=";", dialect="excel")
                csvwriter.writerow(["organization", "success", "date"])
                for reservation in self.sort(reservations):
                    csvwriter.writerow([
                        reservation.organization,
                        reservation.status,
                        datetime.strptime(
                            reservation.date,
                            self.config.date_in_format
                        ).strftime(self.config.date_out_format)
                    ])

            csvfile.close()

        except IOError:
            self.logger.log(
                "Can't open file: '{}'".format(self.config.output_file),
                Logger.LogLevel.ERROR
            )
            sys.exit(1)

        except:  # noqa: E722
            print("Unexpected error", sys.exc_info()[0])
            raise Exception()
