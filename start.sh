#!/bin/bash

cd /home/ledwall/ledwallslab

# Wait 5 seconds before trying to update
sleep 5

# testing internet connection
ping -c 1 -q 8.8.8.8 | grep "1 received"
if [ $? == 0 ]; then
	echo "Connected to the internet, pullin repo \n";
	git pull;
else
	echo "Not connected, start ledwell without pulling \n";
fi

# launch server in background
python3 server/ledwall.py &

# launch simple client to test
#python3 client/strand.py

