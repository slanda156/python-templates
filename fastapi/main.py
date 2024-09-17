import yaml
import logging
import logging.config
import traceback

import uvicorn
from fastapi import FastAPI


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggerConfig)

logger = logging.getLogger(__name__)


from src.routers import user


def main() -> None:
    app = FastAPI(
        title="Default API",
        version="0.1.0"
    )

    app.include_router(
        user.router,
        prefix="/user"
    )

    uvicorn.run(
        "main:app",
        port=8000,
        log_config=loggerConfig
    )


if __name__ == "__main__":
    try:
        main()

    except Exception:
        logger.critical(traceback.format_exc())
