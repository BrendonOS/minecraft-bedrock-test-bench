import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "spiffy",
    version = "0.0.1",
    description = ("A Minecraft: PE server in Python"),
    license = "GPL-3.0",
    keywords = "mcpe raknet minecraft server",
    url = "https://github.com/spiffy/spiffy",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)