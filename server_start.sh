#!/bin/bash
#
# Creates worker and beat services for Celery, starts Django server
# Requires tmux (`sudo apt-get install tmux -y`)
# Problems? try `sudo chmod a+x server_start.sh`

cd CYB_PHYS_CAPSTONE/
tmux new-session -d -s django 'python manage.py runserver'
tmux new-session -d -s celery_worker 'celery -A CYB_PHYS_CAPSTONE worker -l info'
tmux new-session -d -s celery_beat 'celery -A CYB_PHYS_CAPSTONE beat'
cd ..
tmux new-session -d -s outback 'python outbackSerial.py'
