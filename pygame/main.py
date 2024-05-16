import yaml
from logging.config import dictConfig
from logging import getLogger

from src.app import App


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    dictConfig(loggerConfig)
logger = getLogger(__name__)

app = App(fps=60, winSize=(800, 600))

if __name__ == "__main__":
    app.gameloop()
