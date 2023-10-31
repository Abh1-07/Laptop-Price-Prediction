from setuptools import find_packages, setup
from typing import List

HYPHEN_E_Dot = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPHEN_E_Dot in requirements:
            requirements.remove(HYPHEN_E_Dot)
    return requirements


# setup information about the application with the version and keep on updating it with new updates
setup(
    name='Laptop_Prediction_Price',
    version='0.0.1',
    author='Abhishek',
    author_email='vedanshtiwari.07@gmail.com',
    packages=find_packages(),  # To find the packages, whichever folder has __init__.py, consider as package
    install_requires=get_requirements('requirements.txt')  # from this will install all the required packages
)
