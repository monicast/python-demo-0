from setuptools import setup, find_packages
setup(
    name = 'helloworld',
    version = '0.2',
    author = 'Monica Stewart',
    author_email = 'mostew@microsoft.com',
    description = 'Demo script',
    packages = find_packages(),    
    install_requires = ['numpy>=1.15.4', 'matplotlib>=3.0.2'],
)