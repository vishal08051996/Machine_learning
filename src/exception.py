import sys
import traceback
from src.logger import get_logger

logger = get_logger(__name__)

class CustomException(Exception):
    """
    Custom exception class that logs errors with details.
    """
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.message = self.get_detailed_error_message(message, error_detail)
        logger.error(self.message)

    def get_detailed_error_message(self, message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return f"Error in {file_name} at line {line_number}: {message}"

    def __str__(self):
        return self.message
