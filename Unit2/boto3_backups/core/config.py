from pathlib import Path
from os import path, environ

CONFIG_FILE_NAME = 's3_lifecycle_config.json'
CURRENT_DIRECTORY = Path(path.dirname(path.realpath(__file__)))
CONFIG_FILE_PATH = CURRENT_DIRECTORY.parent.joinpath(CONFIG_FILE_NAME)

def is_in_testing_mode():
    """Checks for the TESTING_MODE environment variable, returning whether or not it is set to true."""
    return environ.get('TESTING_MODE', 'false').lower() == 'true'