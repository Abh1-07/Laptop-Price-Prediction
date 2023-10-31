import logging
# log errors, custom raised exceptions
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# a log folder will be create in cwd(), with name - "logs_<LOG_FILE>"
os.makedirs(log_path, exist_ok=True)  # SAYS even if file is there,  in the folder, keep on appending whenever required

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH, 
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",  
                    level=logging.INFO)
