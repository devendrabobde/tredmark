#!/bin/bash

sudo apt-get update -y
sudo apt-get install git -y
sudo apt-get install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
sudo apt install docker-compose
git clone https://github.com/devendrabobde/oroshine.git
ls -ltr
cd oroshine/oroshine_app/
