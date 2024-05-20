#!/bin/bash

# Training script
echo "¡Hi, I'm Antonio Rodriguez Farias!"

# Show details of system
cat /etc/os-release

# More details
uname -a

# Copy file to execute 
cp /home/vagrant/shared/file.run .

# Allow execute file
chmod 700 file.run

# Exec
./file.run

# Finished
echo "Bye Bye ^.^"