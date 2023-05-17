import yaml
import logging
import logging.config

from src.app import App


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggerConfig)

logger = logging.getLogger("logger")


if __name__ == "__main__":
    app = App()
    app.init()
    app.mainloop()
