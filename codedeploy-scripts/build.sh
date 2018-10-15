#!/bin/sh
# read all exported variables and initialize nvm
source ~/.bash_profile
# change working folder
cd /var/www/html/wicloud/web/settings
# copy the setting file
cp /home/ec2-user/wicloud-local/local.py .
# symobolic link overriding existing link
ln -sf local.py settings.py
# change permissions to the main prject folder..
sudo chown -R ec2-user:ec2-user /var/www/html/wicloud/
# .. excluded the log folders
sudo chown apache:apache /var/www/html/wicloud/logs/*
# back to the main project folder
cd /var/www/html/wicloud
# initialize virtualenv
/usr/local/bin/virtualenv django --python /usr/local/bin/python3
# activate virtualenv
. django/bin/activate
# package installation
pip3 install .
# db migrations
dj migrate

#frontend
cd /var/www/html/wicloud/webapp
npm install
webpack --env.NODE_ENV=production
# after building the frontend, upload to s3
dj collectstatic --noinput

# deactivate virtualenv
deactivate


