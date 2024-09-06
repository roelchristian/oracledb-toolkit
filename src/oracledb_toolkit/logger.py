# Logging setup for the project

import logging
import sys
import datetime as dt
import os
from src import config

def setup_logging(logger_name: str) -> logging.Logger:

    logger = logging.getLogger(logger_name)

    # Configure logging

    LOG_DIR = os.path.join(config.PROJECT_ROOT, "logs")
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    LOG_FILE = os.path.join(LOG_DIR, f"{dt.datetime.now().strftime('%Y-%m-%d')}.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - [%(levelname)s] - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )

    return logger