import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # names .log file using current time
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # names path to store logs
os.makedirs(logs_path, exist_ok = True) # creates that log folder

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # defines .log file path

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s", 
    level = logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")