# coding: utf-8

"""
    Open Model Zoo Tools

"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "open_model_zoo-py"
VERSION = "0.0.5"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["pyyaml","requests", "onezoo-py"]

setup(
    name=NAME,
    version=VERSION,
    description="Open Model Zoo Tools",
    author_email="",
    url="https://github.com/openvinotoolkit/open_model_zoo",
    keywords=["Swagger", "OneZoo API"],
    install_requires=REQUIRES,
    packages=".",
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'onezoo_download=downloader:main',
        ],
    },
    long_description="""\
    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501
    """
)
