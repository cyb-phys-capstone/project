#!/bin/bash
#
# Stops worker/beat services for Celery and Django server
# Requires tmux (`sudo apt-get install tmux -y`)
# Problems? try `sudo chmod a+x server_stop.sh`

tmux kill-session -t outback
tmux kill-session -t celery_beat
tmux kill-session -t celery_worker
tmux kill-session -t django
