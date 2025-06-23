from setuptools import setup, find_packages

# read the requirements.txt file and use it to install dependecies
with open("requirements.txt".txt) as f:
    install_requires = f.read().splitlines()

setup(
    name="blkpy",
    description="demo python CLI tool to list block devices",
    packages=find_packages(),
    author="Jose Encarnacion",
    enty_points="""
    [console_scripts]
    blkpy=blkpy.main:main
    """,
    # install_requires=['click=8.2.1']
    version="0.0.1",
    urls="https://github.com/ramses2099/python-cli.git",
)
