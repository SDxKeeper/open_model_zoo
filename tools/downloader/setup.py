# coding: utf-8

"""
    Open Model Zoo Tools

"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "open_model_zoo-py"
VERSION = "0.0.6"
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
    author_email="roman.donchenko@intel.com",
    url="https://github.com/openvinotoolkit/open_model_zoo",
    keywords=["Open", "Model", "Zoo"],
    install_requires=REQUIRES,
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'onezoo_download=downloader.downloader:main',
        ],
    },
    long_description="""\
    Wheel contains tools from Open Model Zoo, mainly downloader
    """
)
