#!/usr/bin/env python3
"""Regex-ing"""

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter data in log message."""
    for field in fields:
        message = re.sub(
            f"{field}=.*?{separator}",
            f"{field}={redaction}{separator}",
            message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = ("[HOLBERTON] %(name)s %(levelname)s "
              "%(asctime)-15s: %(message)s")
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values in incoming log records using filter_datum """
        record.msg = filter_datum(
            self.fields, self.REDACTION,
            record.getMessage(), self.SEPARATOR
        )
        return super().format(record)


if __name__ == '__main__':
    # Example usage
    message = (
        "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
    )
    log_record = logging.LogRecord(
        "my_logger", logging.INFO, None, None, message, None, None
    )
    formatter = RedactingFormatter(fields=("email", "ssn", "password"))
    print(formatter.format(log_record))


# Definition of important PII fields
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Create and return a logger configured to obfuscate PII."""
    # Create the logger
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Configure StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
