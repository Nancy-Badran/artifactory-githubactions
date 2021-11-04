#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description="An example of how to create and publish to pypi.org",
    author="Nancy Badran",
    author_email="nancybadran84@gmail.com",
    url="https://nancytest.jfrog.io/artifactory/api/pypi/default-pypi/simple",
    version="0.1",
    install_requires=["nose",'PyYAML>3.11', 'nltk'],
    packages=["pythonProj","tests"],
    name="pythonProj",
)