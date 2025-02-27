#!/usr/bin/env python3
# Import built-in modules
import yaml
import logging
import logging.config
import traceback
# Import third-party modules
from coloredlogs import install
import uvicorn
from fastapi import FastAPI


with open("logger.yaml") as f:
    loggerConfig = yaml.safe_load(f.read())
    logging.config.dictConfig(loggerConfig)
    log_format = loggerConfig.get("formatters", {}).get("simple", {}).get("format", None)
    install(fmt=log_format)
logger = logging.getLogger(__name__)

# Import local modules
from src.routers import user

# Define the main function
def main() -> None:
    """
    debug: bool - More detailed logs
    title: str - The title of the API
    summary: str - The summary of the API
    description: str - The description of the API
    version: str - The version of the API
    servers: List[Dict[str, str | Any]] - The servers of the API (Production, Development, etc.)
    docs_url: str - The URL of the Swagger documentation (default: /docs None to disable)
    redoc_url: str - The URL of the ReDoc documentation (default: /redoc None to disable)
    swagger_ui_parameters: Dict[str, Any] - The parameters for the Swagger UI
    dependencies: Sequence[Depends] | None - Global dependencies for all routes
    responses: Dict[Union[int, str], Dict[str, Any]] - The default responses for all routes
    on_startup: Sequence[Callable] | None - The functions to run on startup
    on_shutdown: Sequence[Callable] | None - The functions to run on shutdown
    terms_of_service: str | None - The URL of the terms of service
    contact: Union[Dict[str, str], Any] | None - The contact information
    license_info: Dict[str, str | Any] | None - The license information
    """
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


# Run the program if it is the main module
if __name__ == "__main__":
    try:
        main()
    # Log any exceptions
    except Exception:
        logger.critical(traceback.format_exc())
