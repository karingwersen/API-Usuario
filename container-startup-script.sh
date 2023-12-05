#!/bin/sh

nohup mongod &

python3.11 /app/api/api.py
