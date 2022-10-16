#!/usr/bin/env bash

set -o errexit
/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
pip --default-timeout=100 install types-cryptography
poetry install
python manage.py collectstatic --no-input
python manage.py migrate