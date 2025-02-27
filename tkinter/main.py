#!/usr/bin/env python3
# Import built-in modules
import yaml
import logging
import logging.config
import traceback
# Import third-party modules
from coloredlogs import install


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggerConfig)
    log_format = loggerConfig.get("formatters", {}).get("simple", {}).get("format", None)
    install(fmt=log_format)
logger = logging.getLogger(__name__)

# Import local modules
from src.app import App

# Define the main function
def main() -> None:
    app = App()
    app.init()
    app.mainloop()


# Run the program if it is the main module
if __name__ == "__main__":
    try:
        main()
    # Log any exceptions
    except Exception:
        logger.critical(traceback.format_exc())
