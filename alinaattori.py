#!/usr/bin/env python
#
# Here we should have some very toplevel documentation about Alinaattori 2.0
#

from lib.config import Config
from lib.logger import Logger
from lib.arguments import Arguments
from lib.input import Input
from lib.output import Output
from lib.requests import Requests

import sys


def main():
    args = Arguments()
    arguments = args.parse_arguments(sys.argv[1:])

    config = Config(
        arguments["input_file"],
        arguments["output_file"],
        arguments["date_in_format"],
        arguments["date_out_format"],
        arguments["loglevel"]
    )

    logger = Logger(config.loglevel)

    logger.log("Starting Alinaattori 2.0", start="\n")

    reader = Input(config, logger)
    raw_request_data = reader.read()

    requests = Requests(config, logger)
    reservations = requests.process_requests(
        requests.process_raw_request_data(raw_request_data)
    )

    writer = Output(config, logger)
    writer.stdout(reservations)
    writer.file(reservations)

    logger.log("Program finished succesfully", start="\n", end="\n")


main()
