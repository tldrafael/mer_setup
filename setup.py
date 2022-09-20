from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.sdist import sdist
import os, pathlib
from subprocess import check_call


# HERE = pathlib.Path(__file__).parent
HERE = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print("######### HERE ########")
with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()


setup(
    name='mer_setup',
    version='0.1',
    author='Rafael Toledo',
    description='MER Setup',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/tldrafael/mer_setup',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.6',
)

