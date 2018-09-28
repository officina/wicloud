#!/bin/sh
cd /home/ubuntu/mygenerali-bck/web/settings
cp /home/ubuntu/mygenerali-local/bck/local.py .
ln -s local.py settings.py 
sudo chown -R ubuntu:ubuntu /home/ubuntu/mygenerali-bck/
cd /home/ubuntu/mygenerali-bck
virtualenv venv --python /usr/bin/python3
. venv/bin/activate
pip install .
dj migrate
deactivate
