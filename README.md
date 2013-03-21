pilarm
======

An alarm for the Raspberry Pi


Installation
============
Installation is quite easy

	./setup.sh

This installs the dependencies like mplayer. Since sudo commands are used your user needs root privileges.


Usage
=====
So far you can only control the alarm with the console.

	python pilarm.py <time> <audiofile/playlist>

Example 1: You want to be woken up at 10:15

	python pilarm.py 10:15 ~/mp3/somefile.mp3

Example 2: You want to be woken up at 08:00 with a playlist

	python pilarm.py 08:00 ~/mp3/someplaylist.m3u

Don't forget to run the commands in a screen :-)
How to end the alarm? Ctrl+C. So far there is no other possibility (or you can just let the music run and be woken up the next day at the same time)
