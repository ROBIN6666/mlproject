from setuptools import  find_packages,setup
from typing import List

#for trigerring the set.py file
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    :This function will return the list of the requirements
    :param file_path:
    :return:
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirement]

        #It should come in the requirement txt file
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
name='mlproject',
version='0.0.1',
author='Rahul',
author_email='rahulkumark72@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
