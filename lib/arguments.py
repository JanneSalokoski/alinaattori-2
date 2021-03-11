#!/usr/bin/env python


from lib.logger import Logger

import getopt
import sys


class Arguments:
    def display_help(self):
        print("""Usage: alinaattori.py [OPTIONS]
This is a program which does things. Maybe. It should...

Options:
 -h, --help                     print this help
 -s, --silent                   run silently
 -v, --verbose                  print more information to stdout
 -i, --input=INPUT_FILE         read input from INPUT_FILE
 -o, --output=OUTPUT_FILE       write output into OUTPUT_FILE
     --date-in-format=FORMAT    read dates in FORMAT (https://strftime.org/)
     --date-out-format=FORMAT   write dates in FORMAT (https://strftime.org/)
""")

    def parse_arguments(self, argv):
        short_options = "ho:i:vs"
        long_options = [
            "help",
            "output=",
            "input=",
            "verbose",
            "silent",
            "date-in-format=",
            "date-out-format="
        ]

        try:
            arguments, values = getopt.getopt(
                argv,
                short_options,
                long_options
            )

        except getopt.error as err:
            self.logger.log(err, Logger.LogLevel.ERROR)
            sys.exit(1)

        parameters = {
            "loglevel": Logger.LogLevel.LOG,
            "input_file": "input.csv",
            "output_file": "output.csv",
            "email_template": "email_template.txt",
            "date_in_format": "%d.%m.%Y",
            "date_out_format": "%Y-%m-%d"
        }

        for (current_argument, current_value) in arguments:
            if current_argument in ("-h", "--help"):
                self.display_help()
                sys.exit(0)

            elif current_argument in ("-v", "--verbose"):
                parameters["loglevel"] = Logger.LogLevel.DEBUG

            elif current_argument in ("-s", "--silent"):
                parameters["loglevel"] = Logger.LogLevel.SILENT

            elif current_argument in ("-i", "--input"):
                parameters["input_file"] = current_value

            elif current_argument in ("-o", "--output"):
                parameters["output_file"] = current_value

            elif current_argument in ("--date-in-format"):
                parameters["date_in_format"] = current_value

            elif current_argument in ("--date-out-format"):
                parameters["date_out_format"] = current_value

        return parameters
