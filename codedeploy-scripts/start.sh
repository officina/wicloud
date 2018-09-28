#!/bin/sh
cd /home/ubuntu/mygenerali-bck
. venv/bin/activate
nohup dj r 0.0.0.0:8000 >dj.log 2>dj.err &
deactivate
