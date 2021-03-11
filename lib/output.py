#!/usr/bin/env python

from lib.logger import Logger

from datetime import datetime

import csv
import sys
import glob
import os


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

    def read_email_template(self):
        """Read email template"""
        try:
            self.logger.log(
                "Reading email template from file: '{}'"
                .format(self.config.email_template),
                start="\n"
            )

            with open(
                self.config.email_template,
                "r",
                encoding="utf-8-sig"
            ) as template_file:
                return template_file.read()

        except IOError:
            self.logger.log(
                "Can't open file: '{}'".format(self.config.email_template),
                Logger.LogLevel.ERROR
            )
            sys.exit(1)

        except:  # noqa: E722
            print("Unexpected error", sys.exc_info()[0])
            raise Exception()

    def purge_email_directory(self):
        """Remove all files from ./emails/"""
        self.logger.log("Purging files from '{}'".format(
            self.config.email_directory))

        try:
            for file in glob.glob("{}*".format(self.config.email_directory)):
                os.remove(file)

        except IOError:
            self.logger.log(
                "Can't open directory: '{}'".format(
                    self.config.email_directory
                ),
                Logger.LogLevel.ERROR
            )
            sys.exit(1)

        except:  # noqa: E722
            print("Unexpected error", sys.exc_info()[0])
            raise Exception()

    def write_email(self, reservation, template):
        """Print email for organization"""
        self.logger.log(
            "Writing file: '{}{}.txt'".format(
                self.config.email_directory,
                reservation.email
            ),
            Logger.LogLevel.DEBUG
        )

        try:
            with open(
                "{}/{}.txt".format(
                    self.config.email_directory,
                    reservation.email
                ),
                "w+"
            ) as email_file:
                email_file.write(template.format(
                    organization=reservation.organization,
                    date=reservation.date
                ))

        except IOError:
            self.logger.log(
                "Can't open file: '{}'".format(self.config.output_file),
                Logger.LogLevel.ERROR
            )
            sys.exit(1)

        except:  # noqa: E722
            print("Unexpected error", sys.exc_info()[0])
            raise Exception()

    def email(self, reservations):
        """Print emails for organizations"""
        template = self.read_email_template()

        if (not self.config.no_purge):
            self.purge_email_directory()

        if (not self.config.no_email):
            self.logger.log(
                "Writing emails into directory: '{}'".format(
                    self.config.email_directory,
                ),
                start="\n"
            )
            for reservation in reservations:
                if (reservation.status):
                    self.write_email(reservation, template)
