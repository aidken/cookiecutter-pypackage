#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import io
import argparse

# cSpell:ignore levelname


def main():
    arg_parser = argparse.ArgumentParser()
    group = arg_parser.add_mutually_exclusive_group()

    group.add_argument("-a", "--aaa", action="store_true", help="Do AAA.")
    group.add_argument("-b", "--bbb", action="store_true", help="Do BBB.")
    group.add_argument("-c", "--ccc", action="store_true", help="Do CCC.")
    group.add_argument("-d", "--ddd", action="store_true", help="Do DDD.")

    args = arg_parser.parse_args()

    # if no argument is passed, show help
    if len(sys.argv) == 1:
        arg_parser.print_help(sys.stderr)
        sys.exit(1)

    elif args.aaa:
        aaa()
    elif args.bbb:
        bbb()
    elif args.ccc:
        ccc()
    elif args.ddd:
        ddd()
    else:
        arg_parser.print_help()


def aaa():
    logger.debug("func aaa() invoked.")
    print(f'hi from {__name__}.')
    pass


def bbb():
    logger.debug("func bbb() invoked.")
    pass


def ccc():
    logger.debug("func ccc() invoked.")
    pass


def ddd():
    logger.debug("func ddd() invoked.")
    pass


if __name__ == "__main__":
    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    logger = logging.getLogger(__name__)
else:
    logger = logging.getLogger(f"__main__.{__name__}")
logger.setLevel(logging.DEBUG)

format_file = logging.Formatter(
    "%(asctime)s %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s"
)
file_handler = logging.FileHandler(str(sys.argv[0])[:-3] + ".log")
file_handler.setFormatter(format_file)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

# add a Handler which writes INFO messages or higher to the console
format_console = logging.Formatter(
    "%(filename)s: %(levelname)s %(funcName)s - %(message)s"
)
console_handler = logging.StreamHandler()
console_handler.setFormatter(format_console)
console_handler.setLevel(logging.INFO)
logger.addHandler(console_handler)

if __name__ == "__main__":
    main()
