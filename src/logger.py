import logger
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)

## This line is creating the directory specified by log_path. 
## The os.makedirs() function is used to create a directory, 
## and it will also create any necessary intermediate directories 
## if they don't already exist (this is sometimes called "creating directories recursively").
## The exist_ok=True argument means that if the directory already exists, 
## no error will be raised and the function will do nothing.
os.makedirs(LOG_FILE_PATH, exist_ok=True)


## The provided 'format' is the best practice for logging in python.
logger.basicConfig(
    filename=LOG_FILE_PATH,
    level=logger.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
