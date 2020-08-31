#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'somos_kudasai', 'chibi_marshmallow>=0.0.1' ]

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="guarda los resultados de somoskudasai.com en elasticsearch",
    entry_points={
        'console_scripts': [
            'somos_kudasai_elasticsearch=somos_kudasai_elasticsearch.cli:main',
        ],
    },
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='somos_kudasai_elasticsearch',
    name='somos_kudasai_elasticsearch',
    packages=find_packages(include=['somos_kudasai_elasticsearch', 'somos_kudasai_elasticsearch.*']),
    url='https://github.com/dem4ply/somos_kudasai_elasticsearch',
    version='0.0.1',
    zip_safe=False,
)
