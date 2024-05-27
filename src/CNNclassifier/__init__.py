import os
import sys
import logging
'''import os: This module provides functions to interact with the operating system, such as creating directories and handling file paths.
import sys: This module provides access to system-specific parameters and functions, such as standard input and output.
import logging: This module provides functions and classes to implement a flexible logging system, which allows you to track events that happen when some software runs.'''
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "log"
log_filepath = os.path.join(log_dir,"running_log.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("CNNclassifierLogger")
