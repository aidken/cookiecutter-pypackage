#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import io
import argparse

# cSpell:ignore datefmt levelname


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
    pass


def bbb():
    pass


def ccc():
    pass


def ddd():
    pass


if __name__ == "__main__":
    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # logger setup
    filename = str(sys.argv[0])[:-3] + ".log"
    format = "%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)-8s: %(message)s"
    logging.basicConfig(
        filename = filename,
        format   = format,
        datefmt  = "%m-%d %H:%M",
        level    = logging.INFO,
        # level    = logging.DEBUG,
        # level    = logging.ERROR,
    )

    # https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger("").addHandler(console)

    main()
