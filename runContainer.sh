#!/bin/bash

service nginx start;
virtualenv /full-stack-python-docker-image/project;
source /full-stack-python-docker-image/project/bin/activate;
gunicorn --chdir /full-stack-python-docker-image/project app:app -b localhost:8000

