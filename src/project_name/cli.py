"""
Cli module with parameters.
"""

import argparse
import os

from dotenv import load_dotenv
from loguru import logger

from project_name.core import increase


def main():
    """
    CLI entry point.

    For parameters run with ``-h/--help`` argument.
    """
    load_dotenv()
    username = os.getenv("UNAME", default="Unknown")

    parser = argparse.ArgumentParser()

    parser.add_argument("a", type=int, default=0)
    parser.add_argument("-b", type=int, default=1)
    args = parser.parse_args()

    a = args.a
    b = args.b

    logger.info(f"Using as user {username}")

    logger.debug(f"Adding a={a} and b={b}.")

    result = increase(a, b)

    logger.info(f"Result: {a} + {b} = {result}")


if __name__ == "__main__":
    main()
