#!/bin/sh
cd /home/ubuntu/wicloud-bck/web/settings
cp /home/ubuntu/wicloud-local/bck/local.py .
ln -s local.py settings.py
sudo chown -R ubuntu:ubuntu /home/ubuntu/wicloud-bck/
cd /home/ubuntu/wicloud-bck
virtualenv venv --python /usr/bin/python3
. venv/bin/activate
pip install .
dj migrate
deactivate
