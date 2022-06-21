import os
from setuptools import setup
from nvpy import nvpy

setup(
    name = "main",
    version = "1.2",
    author = "Kayden Lee",
    author_email = "kayden@programmer.net",
    description = "",
    license = "BSD",
    url = "https://github.com/leekayden/lionsforge-makeathon",
    packages=['main'],
    entry_points = {
        'console_scripts' : ['main = main.main:main']
    },
    data_files = [
        ('share/applications/', ['vxlabs-main.desktop'])
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
)