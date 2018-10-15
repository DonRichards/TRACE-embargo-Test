#!/usr/bin/python
# -*- coding: utf-8 -*-
# How to update the PIDS.log file
# Go to localhost:8080/fedora/risearch
# find triples > language = spo | Response = N-Triples | Limit = Unlimited
#  Query Text or URL = * <info:islandora/islandora-system:def/scholar#embargo-until> * > launch
# Results will look like:
# <info:fedora/utk.ir.td:1> <info:islandora/islandora-system:def/scholar#embargo-until> "2018-12-16T05:00:00Z"^^<http://www.w3.org/2001/XMLSchema#dateTime> .


import time
from splinter import Browser
import os

# Current working dirrectory
dir_path = os.getcwd()

# SET config section
url = "https://trace.utk.edu/islandora/object/"
######### END SET config section

############ test submissions############
with open("pids.log") as pids:
	with Browser('chrome') as browser:
		print('\n\n\n\tStart looking...')
		for pid in pids:
			browser.visit(url + pid)
			if browser.find_link_by_partial_href('/datastream/PDF/download/citation.pdf'):
				print('\033[91m WARNING -> ' + pid.replace('\n', ' ').replace('\r', '') + 'looks like the pdf is publically avaiable!!\033[0m')
			if browser.find_link_by_partial_href('/datastream/SUPPL_'):
				print('\033[91m WARNING -> ' + pid.replace('\n', ' ').replace('\r', '') + 'looks like the supplemental files are publically avaiable!!\033[0m')
			if browser.find_by_id('embargo-message'):
				print('\t' + pid.replace('\n', ' ').replace('\r', '') + 'Embargo message was found!')
			elif browser.is_text_present("You are not authorized to access this page.", wait_time=0):
				print('\t' + pid.replace('\n', ' ').replace('\r', '') + 'Embargo message was found!')
			else:
				time.sleep(5)
				if browser.find_by_id('embargo-message'):
					print('\t' + pid.replace('\n', ' ').replace('\r', '') + 'Embargo message was found!')
