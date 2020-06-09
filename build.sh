#!/bin/bash

# python libraries
pip3 install pygame
pip3 install mutagen

# build directory
mkdir build
cd build

# create executable
pyinstaller --onefile ../src/music.py

cd dist