#!/bin/bash
export http_proxy='127.0.0.1:8118'
wget http://ipecho.net/plain -O - -q ; echo
python ./test.py
wget http://ipecho.net/plain -O - -q ; echo
echo 'If you get 2 different IPs, everything should be working'