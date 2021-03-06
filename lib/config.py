#!/usr/bin/env python

class Config:
    """Create a data-structure for handling configuration"""

    def __init__(
        self,
        input_file,
        output_file,
        email_template,
        email_directory,
        no_purge,
        no_email,
        no_output,
        date_in_format,
        date_out_format,
        loglevel
    ):
        self.input_file = input_file
        self.output_file = output_file
        self.email_template = email_template
        self.email_directory = email_directory
        self.no_purge = no_purge
        self.no_email = no_email
        self.no_output = no_output
        self.date_in_format = date_in_format
        self.date_out_format = date_out_format
        self.loglevel = loglevel
