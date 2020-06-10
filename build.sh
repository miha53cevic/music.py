#!/bin/bash

# python libraries
sudo pip3 install pygame
sudo pip3 install mutagen
sudo pip3 install pyinstaller

# non sudo if sudo doesn't exist
pip3 install pygame
pip3 install mutagen
pip3 install pyinstaller

# build directory
mkdir build
cd build

# create executable
pyinstaller --onefile ../src/music.py

cd dist