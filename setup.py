from setuptools import setup,find_packages
from typing import List

def get_requirement(file_path:str)->List[str]:
    '''
    Function will return the list of packeges present in requirement.txt
    '''
    requirement = []

    hypen_e_dot = "-e ."

    with open(file_path) as file_obj:
        requirement = file_obj.readlines() # read the Line by Line code in Requirement.txt
        requirement = [req.replace("\n"," ") for req in requirement] 
        # remove the \n from the line because when moving to the next line we will get /n we have remove 
        if hypen_e_dot in requirement:
            requirement.remove(hypen_e_dot)
    return requirement

setup(
    name = "my_package",
    version = "0.0.1",
    author='Mohan',
    author_email="Mohangola47@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirements.txt"),
    description = "This is my first package"
)

