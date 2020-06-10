# music.py

## Usage
### Playing a music file (.ogg .mp3)
```bash
    music song.mp3
```
### Result
```bash
    music song.mp3

    Playing... ./song.mp3 at volume: 1.0
    -------------------------------------
    >> Time: 00:53 - 01:00
```
## Options
### --volume
```bash
    music song.mp3 --volume 0.5
```
### --random
Plays a random song inside a given folder (default only .mp3)
```bash
    music ${somefolder} --random
```
### --extension
```bash
    music ${somefolder} --random --extension mp3
```
Used together with random to specify which extension to look for (default .mp3)

## Install
```bash
    cd musicpy
    pip3 install .
```