from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = '-e .'


def get_requirements(file_path) -> List[str]:
    '''
    this function returns the list of required packages for the project '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='Emo_kid',
    version='0.0.1',
    author='Abhishek S A',
    author_email='abhishek.s.a2201@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
