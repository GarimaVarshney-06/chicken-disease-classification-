import os
from pathlib import Path
import logging

# Setting up logging to display messages with the specified format and log level
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

# Defining the project name
project_name = "CNNclassifier"

# Listing all the files and directories that we want to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",   #constructor file so that we can call it
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    
    "dvc.yaml",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Looping through each file path in the list
for filepath in list_of_files:
    # Converting the file path to a Path object(window path)
    filepath = Path(filepath)
    
    # Splitting the file path into directory and file name
    filedir, filename = os.path.split(filepath)
    
    # If the directory part is not empty, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        # If the file already exists and is not empty, log that it already exists
        logging.info(f"{filename} is already exists")
