#!/usr/bin/python

import os, sys, logging

from mplayer import Player

player = Player()
player.loadfile('../mp3/good_charlotte_-_we_believe__matthew_adams_true_sadness_mix.mp3')

def input():
	logging.debug("Foobar")

while True:
	input()
