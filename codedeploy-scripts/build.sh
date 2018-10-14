#!/bin/sh
source ~/.bash_profile
cd /var/www/html/wicloud/web/settings
cp /home/ec2-user/wicloud-local/local.py .
ln -s local.py settings.py
sudo chown -R ec2-user:ec2-user /var/www/html/wicloud/
cd /var/www/html/wicloud
/usr/local/bin/virtualenv django --python /usr/local/bin/python3
. django/bin/activate
pip3 install .
dj migrate
dj collectstatic --noinput
deactivate
cd webapp
npm install
webpack


