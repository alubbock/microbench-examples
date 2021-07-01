#!/bin/sh

# Create virtual environment
/usr/bin/env python -m venv mbenv

# Install the requirements.txt file into mbenv
mbenv/bin/pip install -r requirements.txt
