import re
from pathlib import Path
from logging import getLogger
from packaging.version import Version
from typing import Any

import json
from pydantic import BaseModel, Field, field_validator, ValidationError


VERSION = Version("0.0.0dev0")
logger = getLogger(__name__)
DICTDEFAULTS: dict[str, dict[Any, Any]] = {

}
CONFIGFILE = Path.cwd() / "config.json"
BASICURLRE = re.compile(
    r"^(?:(?:http|https)://)"
    r"(?:"
      r"(?:"
        r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"
        r"[A-Za-z]{2,63}"
      r")"
      r"|"
      r"(?:"
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\."
        r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
      r")"
    r")"
    r"(?::(?:6553[0-5]|655[0-2]\d|65[0-4]\d\d|6[0-4]\d{3}|[1-5]?\d{1,4}))?"
    r"$"
)


class Config(BaseModel):
    pass


    @staticmethod
    def _checkKeys(d: dict, defaults: dict) -> None:
        invalidKeys: list[str] = []
        missingKeys: list[str] = []
        for key in d.keys():
            if key not in defaults:
                invalidKeys.append(key)
        for defaultKey in defaults.keys():
            if defaultKey not in d:
                missingKeys.append(defaultKey)
        if len(invalidKeys) > 0:
            logger.warning(f"Invalid keys in config: {', '.join(invalidKeys)}")
        if len(missingKeys) > 0:
            logger.info(f"Missing keys in config: {', '.join(missingKeys)}")
        for missingKey in missingKeys:
            d[missingKey] = defaults[missingKey]
        for invalidKey in invalidKeys:
            del d[invalidKey]


    def save(self) -> None:
        if CONFIGFILE.exists() and not CONFIGFILE.is_file():
            raise RuntimeError("config.json is not a file! Aborting.")
        try:
            with open(CONFIGFILE, "w", encoding="utf-8") as f:
                json.dump(self.model_dump(), f, ensure_ascii=False, indent=4)
        except PermissionError as e:
            logger.error(f"Permission error saving config")
            raise


    @classmethod
    def load(cls, skipCreate: bool = False) -> "Config":
        if CONFIGFILE.exists() and not CONFIGFILE.is_file():
            raise RuntimeError("config.json is not a file! Aborting.")
        if not CONFIGFILE.exists():
            logger.warning("config.json does not exist!")
            if not skipCreate:
                logger.info("Creating default config.json")
                return cls.createDefault()
        try:
            with open(CONFIGFILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing config.json: {e}")
            if not skipCreate:
                logger.info(f"Creatiing a backup of the invalid {CONFIGFILE.name} as {CONFIGFILE.name}.bak")
                return cls.createDefault()
            else:
                raise
        else:
            logger.info("Config loaded successfully")
            config = cls(**data)
            config.save()
            return config


    @staticmethod
    def _validateBasicUrl(url: str) -> bool:
        return BASICURLRE.fullmatch(url) is not None


    @classmethod
    def createDefault(cls) -> "Config":
        config = cls()
        config.save()
        return config


CONFIG = Config.load()
