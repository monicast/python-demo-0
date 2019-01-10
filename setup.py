
from setuptools import setup, find_packages
setup(
    name = 'imagefun',
    version = '0.1',
    author = 'Monica Stewart',
    author_email = 'mostew@microsoft.com',
    description = 'Demo script',
    packages = find_packages(),    
    install_requires = ['numpy>=1.15.4', 'matplotlib>=3.0.2', 'opencv-python>=3.4.2'],
    package_data={'image_fun': ['haarcascade_frontalface_default.xml']},
    include_package_data=True
)