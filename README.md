mpi3
====

A music player with alarm functionality for the Raspberry Pi. Comes with web interface!


Installation
============
Installation is quite easy

	./setup.sh

This installs the dependencies like mplayer. Since sudo commands are used your user needs root privileges.


Usage
=====
So far only alarm functionality is implemented and right now you need to give a time and audiofile/playlist when starting. Since the webinterface listens on port 80 you need to run the pilarm as root

	sudo ./mpi3.py <time> <audiofile/playlist>

Example 1: You want to be woken up at 10:15

	sudo ./mpi3.py 10:15 ~/mp3/somefile.mp3

Example 2: You want to be woken up at 08:00 with a playlist

	sudo ./mpi3.py 08:00 ~/mp3/someplaylist.m3u

Don't forget to run the commands in a screen :-)

Web Interface
============
pilarm comes with a (so far very basic) web interface which lets you control the alarm. If your Raspberry Pi's ip adress is 192.168.1.9, you can reach the web interface at

	http://192.168.1.9
	
Make sure you have Javascript turned on and that you use a browser that supports WebSockets (every modern browser does). The web interface's style is mobile-first, so you can also use it with your smartphone.
