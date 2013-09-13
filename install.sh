#!/bin/bash
sudo apt-get update -y
sudo apt-get install python-pip -y
sudo apt-get install libxml2-dev -y
sudo apt-get install libxslt1-dev -y
sudo apt-get install python-dev -y
sudo pip install lxml
sudo pip install scrapy
sudo apt-get install tor -y
sudo apt-get install privoxy -y
sudo sed -i '/127.0.0.1:9050/s/^#//' /etc/privoxy/config
sudo service privoxy restart
sudo sed -i '/ControlPort 9051/s/^#//' /etc/tor/torrc
sudo sed -i '/CookieAuthentication 1/s/^#//' /etc/tor/torrc
sudo sed -i '/#HashedControlPassword/s/#HashedControlPassword.*/HashedControlPassword 16:FA312271EB23D48C60F225A74AD2D241186B82912A56892EE64E46C21B/' /etc/tor/torrc
sudo service tor restart
sudo pip install stem