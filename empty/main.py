import yaml
import logging
import logging.config
import traceback


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggerConfig)

logger = logging.getLogger("logger")


if __name__ == "__main__":
    try:
        pass

    except Exception:
        logger.critical(traceback.format_exc())

    finally:
        pass
