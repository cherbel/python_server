#!/bin/bash
cp test_settings.py settings.py
pip3 install --upgrade pip
pip3 install pipenv
pipenv install --ignore-pipfile
