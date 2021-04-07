#!/bin/bash
cp test_settings.py settings.py
pip install --upgrade pip3
pip install pipenv
pipenv install --ignore-pipfile
