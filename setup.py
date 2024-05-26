import setuptools
#  This module is used for packaging Python projects. It provides tools to build and distribute Python packages.
# Reading the content of README.md file as the long description for the package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Defining the version of the package
__version__ = "0.0.0"

# Defining various metadata about the package
REPO_NAME = "chicken-disease-classification-"
AUTHOR_USER_NAME = "GarimaVarshney-06"
SRC_REPO = "CNNclassifier"
AUTHOR_EMAIL = "gungunvarshney00@gmail.com"

# Setting up the package using setuptools
setuptools.setup(
    name=SRC_REPO,  # The name of the source repository
    version=__version__,  # The version of the package
    author=AUTHOR_USER_NAME,  # The author's username
    author_email=AUTHOR_EMAIL,  # The author's email address
    description="A small python package for CNN app",  # A short description of the package
    long_description=long_description,  # The long description read from README.md
    long_description_content="text/markdown",  # The format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # The URL of the repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # The URL for the bug tracker
    },
    package_dir={"": "src"},  # The directory where the packages are located
    packages=setuptools.find_packages(where="src")  # Automatically find packages in the specified directory
)
