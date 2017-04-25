#!/bin/bash
#
# Demo of project
while [ : ]
do
    ./server_start.sh && sleep 6s && ./server_stop.sh && sleep 1s
done
