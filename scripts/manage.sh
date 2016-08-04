#!/usr/bin/env bash

export WORKON_HOME=/var/envs
export PROJECT_HOME=/var/www/vern
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
export PIP_RESPECT_VIRTUALENV=true
export IS_LOCAL=True

source /var/envs/news/bin/activate

cd /var/www/news

python manage.py "$@"