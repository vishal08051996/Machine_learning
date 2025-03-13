from setuptools import setup, find_packages

# Read dependencies from requirements.txt
def read_requirements():
    with open("requirements.txt") as req_file:
        listing =[i.replace("\n","") for i in req_file.readlines()] 
        if "-e ." in listing:
            listing.remove("-e .")
        return listing

setup(
    name="construction_strength_prediction",
    version="0.1",
    packages=find_packages(),
    install_requires=read_requirements(),
    author="Vishal Jadhaav",
    description="A machine learning model to predict building strength based on construction parameters",
)
