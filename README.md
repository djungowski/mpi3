mpi3
====

A music player with alarm functionality for the Raspberry Pi. Comes with web interface!


Installation
============
Installation is quite easy

	./setup.sh

This installs the dependencies like mplayer. Since sudo commands are used your user needs root privileges.


Running mpi3
============
Since the webinterface listens on port 80 you need to run the pilarm as root. If you want to change the http port you can do so in the config.ini in the http section

	sudo ./mpi3.py

If you want to run mpi3 in the debug mode you can do so by running

	sudo ./mpi3.py --debug
	
If you want to run mpi3 with a mocked player (in case you can't use mplayer - this should be used for development only):

	sudo ./mpi3.py --mock-player

If you want to run mpi3 as daemon

	sudo ./mpi3.py -d

If you want to handle mpi3 via /etc/init.d and start it automatically when your Raspberry Pi boots, just run the install-init-script.sh script from the init.d directory

	cd init.d
	./install-init-script.sh

Again, root privileges are required (see installation) 

Web Interface
============
mpi3 comes with a (so far very basic) web interface which lets you control the alarm. If your Raspberry Pi's ip adress is 192.168.1.9, you can reach the web interface at

	http://192.168.1.9
	
Make sure you have Javascript turned on and that you use a browser that supports WebSockets (every modern browser does). The web interface's style is mobile-first, so you can also use it with your smartphone.

Notes
=====
Background taken from http://pixgood.com/sketchy-background.html
