from setuptools import find_packages, setup
#import os
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return the list of requirements

    Args
        file_path
    
    Returns
    """
    requirements = []
    #with os.open(file_path, 'r') as file_obj:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            #pass
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name="0760_20_01_ML_Students_Performance",
    version='0.0.1',
    author='Luismbpr',
    author_email='NaN@gmail.com',
    packages= find_packages(),
    #install_requires=['pandas', 'numpy'],
    install_requires=get_requirements(file_path='requirements.txt')

)

