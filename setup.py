#!/usr/bin/env python

import os
import sys

from setuptools import setup
from setuptools import find_packages

sys.path.append(
    os.path.join(os.path.dirname(__file__))
)

import statology

setup(
    name = "forexrates",
    version = statology.__version__,
    author = "shark-utilities developers",
    author_email = "neuralNOD@outlook.com",
    description = "A unified codebase for fetching FOREX rates.",
    # long_description = open("README.md", "r").read(),
    # long_description_content_type = "text/markdown",
    url = "https://github.com/sharkutilities/statology",
    packages = find_packages(
        exclude = ["tests*", "examples*"]
    ),
    install_requires = [
        "numpy>=2.3.5",
        "scipy==1.17.1",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls = {
        "Issue Tracker" : "https://github.com/sharkutilities/statology/issues",
        # "Code Documentations" : "https://.readthedocs.io/en/latest/index.html",
        "Org. Homepage" : "https://github.com/sharkutilities"
    },
    keywords = [
        # keywords for finding the package::
        "statistics", "outliers", "pandas", "numpy", "scipy",
        # keywords for finding the package relevant to usecases::
        "wrappers", "data science", "data analysis", "data scientist", "data analyst"
    ],
    python_requires = ">=3.11"
)
