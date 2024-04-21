import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

LOG_FOLDER = os.path.join(os.getcwd(), "logs")

## This line is creating the directory specified by log_path. 
## The os.makedirs() function is used to create a directory, 
## and it will also create any necessary intermediate directories 
## if they don't already exist (this is sometimes called "creating directories recursively").
## The exist_ok=True argument means that if the directory already exists, 
## no error will be raised and the function will do nothing.
os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE_NAME)

## The provided 'format' is the best practice for logging in python.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__" : 
    logging.debug("This is a debug message")