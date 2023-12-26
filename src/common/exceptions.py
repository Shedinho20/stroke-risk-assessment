"""
Custom Exception Handler
"""


def error_message_detail(error, exc_tb):
    """
    Generate a descriptive error message.
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script '{file_name}' at line number {exc_tb.tb_lineno}: {error}"

    return error_message


class CustomException(Exception):
    """
    Custom Exception class to generate detailed error messages.

    Args:
    - error_message: The error message.
    - exc_tb: Traceback information associated with the error.

    Attributes:
    - error_message (str): A formatted error message including file name, line number, and error description.
    """

    def __init__(self, exc_tb, error_message="Something wnet wrong"):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, exc_tb)

    def __str__(self):
        return self.error_message
