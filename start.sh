#!/bin/bash

cd /home/ledwall/ledwall

# testing internet connection
ping -c 1 -q 8.8.8.8 | grep "1 received"
if [ $? == 0 ]; then
	echo "pulling repository :)";
	git pull;
else
	echo "no connection : can't pull repository :'(";
fi

# launch server in background
python3 server/ledwall.py &

# launch simple client to test
#python3 client/strand.py

