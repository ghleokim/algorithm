#! usr/bin/bash

today=$(date +"%y%m%d")
cur=$(pwd)

if [ ! -d ${cur}/${today} ]; then
	mkdir -p ${cur}/${today}
	mkdir -p ${cur}/${today}/input
	echo "directory ${today}/ made"
else
	echo "directory ${today} already exists."
fi
