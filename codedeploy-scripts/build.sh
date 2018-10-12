#!/bin/sh
cd /var/www/wicloud/web/settings
cp /home/ec2-user/wicloud-local/local.py .
ln -s local.py settings.py
sudo chown -R ec2-user:ec2-user /var/www/wicloud/
cd /var/www/wicloud
virtualenv django --python /usr/bin/python3
. venv/bin/activate
pip install .
dj migrate
deactivate
