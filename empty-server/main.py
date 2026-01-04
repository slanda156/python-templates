#!/usr/bin/env python3
# Import built-in modules
import logging
# Import third-party modules

# Import local modules
from src import createCrashLog
import src.app

logger = logging.getLogger(__name__)

# Define the main function
def main() -> None:
    5/0


# Run the program if it is the main module
if __name__ == "__main__":
    try:
        main()
    # Log any exceptions
    except Exception as e:
        logger.critical("An unhandled exception occurred:", exc_info=True)
        createCrashLog(e)
        raise
