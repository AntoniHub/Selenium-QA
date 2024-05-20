#!/bin/bash

# jp2a: Convert images into ASCII art
sudo apt install jp2a
jp2a --output=ascii.txt --colors input.png
