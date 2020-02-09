#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
import os
from io import open as io_open
from {{cookiecutter.project_slug}} import __PKG_NAME__, __PROJECT_CLASS_MAIN__


{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}


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
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    description='{{cookiecutter.project_short_description}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    license='{{cookiecutter.open_source_license}}',
    maintainer='{{cookiecutter.full_name}}',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url=f'https://pypi.org/project/{__PKG_NAME__}/',
    packages=find_packages(include=['{{cookiecutter.project_slug}}', '{{cookiecutter.project_slug}}.*']),
    platforms=['any'],
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        {%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
        {%- endif %}
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
    keywords='{{cookiecutter.project_slug}} hello world helloworld console',
    entry_points={'console_scripts': [f'{__PKG_NAME__}={{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}:{__PROJECT_CLASS_MAIN__}']},
    package_data={'{{cookiecutter.project_slug}}': ['data/data.json']}
)
