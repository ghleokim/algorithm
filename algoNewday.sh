#! usr/bin/bash

today=$(date +"%y%m%d")

if [ ! -d ~/algo/${today} ]; then
	mkdir -p ~/algo/${today}
	mkdir -p ~/algo/${today}/input
	echo "directory ${today}/ made"
else
	echo "directory ${today} already exists."
fi
