import logging
from sys import exit

def info(message: str):
    """Shows a info level message
    Args:
        message: The info message you want to shows up    
    """
    logging.info(message)

def error(message: str, do_exit: bool =True):
    """Shows an error level message and then exit with a non 0 status code
    Args:
        message: The error message you want to shows up  
        do_exit: Whether to perform an system exit 
    """
    logging.error(message)
    if do_exit:
        exit(10)

def warning(message: str):
    """Shows a warning level message
    Args:
        message: The warning message you want to shows up  
    """
    logging.warning(message)