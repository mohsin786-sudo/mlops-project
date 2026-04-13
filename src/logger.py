import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

log_file = f"{datetime.now().strftime('%Y -%m-%d')}.log"
log_path = os.path.join(LOG_DIR, log_file)


logging.basicConfig(
    filename=log_path,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    

)