=========
Phonebook
=========

This module can detect inconsistent lists of phone numbers.

Installation
============
We suggest you first create a virtual environment using

    python -m venv venv

Check the `Python documentation <https://docs.python.org/3/library/venv.html>`_ for how to activate this environment on your platform. Then install this module:

    python setup.py install

Usage
=====

    python phonebook < input_data.csv

for more information see the docs directory.

Self-tests
==========
Run the self-tests using pytest:

    python -m pytest