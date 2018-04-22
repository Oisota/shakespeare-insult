from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='Shakespeare Insult',
        version='1.0.0',
        description='Generate insults in the style of Bill Shakespeare',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Derek Morey',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Operating System :: OS Independent',
            ],
        keywords=['William Shakespeare', 'Shakespeare', 'insult'],
        py_modules=['bill']
        )
