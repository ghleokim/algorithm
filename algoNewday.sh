#! usr/bin/bash

today=$(date +"%y%m%d")
cur=$(pwd)

# check if directory exists
if [ ! -d ${cur}/${today} ]; then
	mkdir -p ${cur}/${today}
	echo "directory ${today}/ made"
else
	echo "directory ${today} already exists."
fi

# check if test file exists
if [ ! -f ${cur}/${today}/test.py ]; then
	touch ${cur}/${today}/test.py
	echo "file ${today}/test.py made"
else
	echo "file ${today}/test.py already exists."
fi
