"""Modules"""
from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."


def get_requirements() -> list[str]:
    """
    Return a list of requirements
    """
    requirements = []
    with open("requirements.txt", encoding="utf-8") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="stroke-risk-assessment",
    version="0.01",
    author="Shedrach Ezenwali",
    author_email="shedinhoshedrach@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
