from setuptools import setup, find_packages

setup(
    name='remoteweb',
    version='0.1',
    packages=find_packages(),
    install_requires=['pypdf'],
    include_package_data=True,
)