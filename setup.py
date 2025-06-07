from setuptools import setup, find_packages
from typing import List
from pathlib import Path

def get_requirements(file_path: str)-> List[str]:
    '''
    Return the list of requirements for this project
    '''
    file = Path(file_path)
    if file.exists():
        with file.open("r") as requirement_file:
            requirements = [line.strip() for line in requirement_file]
        requirements.pop()
    
    print(requirements)

setup(
    name="my_package",
    version="0.0.1",
    author="SakthiSelvan",
    description="A simple example package",
    packages=find_packages(),   # Automatically find sub-packages
    install_requires= get_requirements('requirements.txt')
)
