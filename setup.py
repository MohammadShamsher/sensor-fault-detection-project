from setuptools import setup, find_packages

from typing import List

def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    requirements: List[str] = []

    with open(file_path, "r") as file:
        for line in file:
            req = line.strip()

            # skip empty lines, comments, and editable installs
            if not req or req.startswith("#") or req.startswith("-e"):
                continue

            requirements.append(req)

    return requirements
setup(
    name="sensor",
    version="0.0.1",
    author="shamsher",
    packages=find_packages(),
    install_requires=get_requirements()
    )