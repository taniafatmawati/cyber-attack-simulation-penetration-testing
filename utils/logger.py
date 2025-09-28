#!/usr/bin/env python3
import logging
import os

def setup_logger(name="cyber_sim", log_file=None, level=logging.INFO):
    """
    Create a logger instance that writes both to stdout and to logs/<name>.log by default.
    """
    os.makedirs("logs", exist_ok=True)

    if log_file is None:
        log_file = os.path.join("logs", f"{name}.log")

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if called multiple times
    if not logger.handlers:
        fh = logging.FileHandler(log_file)
        ch = logging.StreamHandler()

        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
