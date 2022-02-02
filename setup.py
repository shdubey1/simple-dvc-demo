from ensurepip import version
from importlib.resources import Package
from tabnanny import verbose
from unicodedata import name
from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.0.1",
    description="its a wine Q package",
    author="shdubey1",
    Packages=find_packages(),
    license="MIT"

)