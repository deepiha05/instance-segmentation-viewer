
from setuptools import setup, find_packages
setup(name="newmypackage",
version="0.4",
description="Image dataset, transforms, Mask R-CNN wrapper and visualisation used by the Tkinter image viewer",
author="Deepiha",
packages=find_packages(include=['newmypackage', 'newmypackage.*']),
install_requires=['torch', 'torchvision', 'numpy', 'pillow', 'matplotlib'])
