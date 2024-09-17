import yaml
import logging
import logging.config
import traceback

from src.app import App


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggerConfig)

logger = logging.getLogger(__name__)


def main() -> None:
    app = App(fps=60, winSize=(800, 600))
    app.gameloop()


if __name__ == "__main__":
    try:
        main()

    except Exception:
        logger.critical(traceback.format_exc())
