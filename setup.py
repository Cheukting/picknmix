#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []
extras_requirements = {'test': ['pytest', 'scikit-learn>=0.21.2']}

setup(
    author="Cheuk Ting Ho",
    author_email='cheukting.ho@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A simple tool to help building stacking models.",
    entry_points={
        'console_scripts': [
            'picknmix=picknmix.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='picknmix',
    name='picknmix',
    packages=find_packages(include=['picknmix']),
    extras_require=extras_requirements,
    url='https://github.com/Cheukting/picknmix',
    version='0.1.3',
    python_requires=">=3.5",
    zip_safe=False,
)
