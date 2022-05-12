#!/bin/bash

set -m
# Start the first process
gunicorn gcptest.wsgi:application --bind 0.0.0.0:8000 &
  
# Start the second process
python pubsub_subscribe.py 
  
# now we bring the primary process back into the foreground
# and leave it there
fg %1