#!/bin/bash
cp test_settings.py settings.py
python -m pip install --upgrade pip
pip3 install pipenv
pipenv install --ignore-pipfile
