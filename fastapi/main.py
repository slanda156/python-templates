import uvicorn
import yaml
import logging
import logging.config
from fastapi import FastAPI


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggerConfig)


from src.routers import user


app = FastAPI(
    title="Homesite API",
    version="0.1.0"
)

app.include_router(
    user.router,
    prefix="/user"
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=8000,
        log_config=loggerConfig
    )
