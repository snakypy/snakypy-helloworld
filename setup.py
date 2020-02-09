#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
import os
from io import open as io_open
from snakypy_helloworld import __PKG_NAME__, __PROJECT_CLASS_MAIN__


"""
    Long description
"""
with open("README.rst", "r") as f:
    long_description = f.read()

"""
    Extras Requires
"""
src_dir = os.path.abspath(os.path.dirname(__file__))
extras_require = {}
requirements_dev = os.path.join(src_dir, 'requirements-dev.txt')
with io_open(requirements_dev, mode='r') as fd:
    extras_require['dev'] = [i.strip().split('#', 1)[0].strip()
                             for i in fd.read().strip().split('\n')]

setup(
    name='snakypy_helloworld',
    version='1.0.0',
    description='Snakypy HelloWorld is a simple Python script to require Hello messages from the console.',
    author='Snakypy Org',
    author_email='contact.snakypy@gmail.com',
    license='MIT license',
    maintainer='Snakypy Org',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url=f'https://pypi.org/project/{__PKG_NAME__}/',
    packages=find_packages(include=['snakypy_helloworld', 'snakypy_helloworld.*']),
    platforms=['any'],
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
    keywords='snakypy_helloworld hello world helloworld console',
    entry_points={'console_scripts': [f'{__PKG_NAME__}=snakypy_helloworld.snakypy_helloworld:{__PROJECT_CLASS_MAIN__}']},
    package_data={'snakypy_helloworld': ['data/data.json']}
)
