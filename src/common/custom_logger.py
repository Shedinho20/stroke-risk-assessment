import logging
import os
from datetime import datetime


# Todo: Log error to mongodb.
class CustomLogger:
    """Custom logger with mongodb"""

    _instance = None
    _initialized = None
    _is_production = os.getenv("APP_ENV") == "production"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)
            file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
            logs_path = os.path.join(os.getcwd(), "logs")
            os.makedirs(logs_path, exist_ok=True)
            log_file_path = os.path.join(logs_path, file_name)

            handler = logging.FileHandler(log_file_path)
            formatter = logging.Formatter(
                "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

            self._initialized = True

    def log_error(self, message, exc_info: bool = False):
        """Log an error"""
        self.logger.error(message, exc_info=exc_info)

    def log_info(self, message):
        """Log an info"""
        self.logger.info(message)
