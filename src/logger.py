import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
## Hardcoded the path - later on use the code above
LOG_PATH_NEW='/Users/luis/Documents/Programming/dev/0760 Complete MLOps Bootcamp With 10 Plus End To End ML Projects Krish Naik/venv_0760_Complete_MLOps_Bootcamp_Krish_Naik_312_01/0760_Course/Section 20 End To End DS Project implementation With Mulitple AWS, Azure Deployment/0760_20_01_ML_Students_Performance/'
logs_path=os.path.join(LOG_PATH_NEW,"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


## Code to test if logger works
#if __name__=="__main__":
#    logging.info("Logging has started")