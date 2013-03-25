mpi3
====

A music player with alarm functionality for the Raspberry Pi. Comes with web interface!


Installation
============
Installation is quite easy

	./setup.sh

This installs the dependencies like mplayer. Since sudo commands are used your user needs root privileges.


Start mpi3
=========
Since the webinterface listens on port 80 you need to run the pilarm as root. If you want to change the http port you can do so in the config.ini in the http section

	sudo ./mpi3.py

If you want to run mp3i in the debug mode you can do so by running

	sudo ./mpi3.py --debug

Don't forget to run the command in a screen :-) (daemon will come someday)

Web Interface
============
pilarm comes with a (so far very basic) web interface which lets you control the alarm. If your Raspberry Pi's ip adress is 192.168.1.9, you can reach the web interface at

	http://192.168.1.9
	
Make sure you have Javascript turned on and that you use a browser that supports WebSockets (every modern browser does). The web interface's style is mobile-first, so you can also use it with your smartphone.
