import os
import sys
from pathlib import Path
import requests
from zipfile import ZipFile
#from dotenv import load_dotenv
#load_dotenv()

#from src.logger import logging
#from src.exception import CustomException
#from src.utils import download_data_github
#from logger import logging
#from exception import CustomException
#from utils import download_data_github

sys.path.append('src/exception/')

#print(f"GITHUB_USERNAME:\n{os.getenv("GITHUB_USERNAME")}")

#getmddd = os.path.join(os.getenv('GITHUB_USERNAME'),os.getenv('GITHUB_USERNAME002'))
#print(getmddd)## Returns: Luismbpr/JOHNDOE

dataset_url= "https://raw.githubusercontent.com/Luismbpr/datasets_001/refs/heads/main/datasets/students_performance_0760.csv"


file_name='students_performance_0760.csv'
#path_to_save='/Users/luis/Documents/Programming/dev/0760 Complete MLOps Bootcamp With 10 Plus End To End ML Projects Krish Naik/venv_0760_Complete_MLOps_Bootcamp_Krish_Naik_312_01/0760_Course/Section 20 End To End DS Project implementation With Mulitple AWS, Azure Deployment/venv_0760_20_01_312_001/0760_20_01_ML_Students_Performance/notebooks/data/'

path_to_save_nofilename= os.path.join(os.getcwd(), 'notebooks','data')

def download_data_github(url:str,path_to_save:str, filename_tosave:str):
    """
    ```
    def download_data_github(url:str,path_to_save:str,is_repo_private:bool=False):
    If repository is private need to add
    import requests
    from requests.structures import CaseInsensitiveDict
    headers = CaseInsensitiveDict()
    headers['Authorization'] = "Add private token here"
    resp = requests.get(url, headers=headers)
    print(resp.status_code)
    ```

    from src.utils import download_data_github
    download_data_github(url=,path_to_save=)
    """
    try:
        #pass
        ## Create directories if they do not exist
        #logging.info(f"src/utils/download_data_github")
        if not os.path.exists(path_to_save):
        #if not os.path.isdir(path_to_save):
            os.makedirs(path_to_save, exist_ok=True)
        
        ### Get content from website and save it
        resp = requests.get(url)
        with open(os.path.join(path_to_save,filename_tosave), 'wb') as file:
            print("Writing contents in file")
            file.write(resp.content)
        #logging.info(f"Downloaded data from Github successfully")

    except Exception as e:
        raise CustomException(e, sys)
#path_to_save_wfilename = os.path.join(os.getcwd(),'notebooks','data', file_name)
#print(f"path_to_save:\n{path_to_save_wfilename}")

try:
    #logging.info(f"data_gathering: Trying to gather and download file: {file_name} from GitHub.")
    download_data_github(url=dataset_url,path_to_save=path_to_save_nofilename, filename_tosave=file_name)
    #logging.info(f"data_gathering: successfully downloaded data from GitHub.")
except Exception as e:
    raise CustomException(e, sys)



#timeout = 10
#url = os.getenv("ORIGINAL_DATA_PATH_ONLINE")
#r = requests.get(url=url, timeout=timeout)
#try:
#    if r.ok:
#        print(f"File found: {r.content}")
#        with ZipFile(r.content) as f:
#            for file in f.namelist():
#                if file.endswith(file_name):
#                    print(f"File found: {r.content}")
#                    data = f.read(f)

#    else:
#        pass
#except Exception as e:
#    raise CustomException(e, sys)