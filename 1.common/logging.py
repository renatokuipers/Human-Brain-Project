# Logging utilities for tracking and debugging

import logging
from logging.handlers import RotatingFileHandler
import os

# Constants for logging
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "BrainSimulationProject.log"
MAX_LOG_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
BACKUP_COUNT = 5  # Number of backup logs to keep

def setup_logger(name=__name__, log_file=LOG_FILE, level=logging.DEBUG, file_log_level=logging.INFO):
    """Set up a logger for the BrainSimulationProject.

    Args:
        name (str): Name of the logger.
        log_file (str): File path for the log file.
        level (int): Logging level for the console handler.
        file_log_level (int): Logging level for the file handler.
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create file handler for log file with rotation
    file_handler = RotatingFileHandler(log_file, maxBytes=MAX_LOG_FILE_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setLevel(file_log_level)

    # Create formatter
    formatter = logging.Formatter(LOG_FORMAT)

    # Add formatter to handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    if not logger.handlers:  # Avoid adding handlers multiple times
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

# Example usage:
# logger = setup_logger(__name__)
# logger.debug("This is a debug message.")
# logger.info("This is an info message.")
# logger.warning("This is a warning message.")
# logger.error("This is an error message.")
# logger.critical("This is a critical message.")
