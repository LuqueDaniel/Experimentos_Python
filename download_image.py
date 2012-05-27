#!/usr/bin/env python
#*-* encoding: utf-8 *-*

import urllib
import sys

contador = 1
base_url = sys.argv[1]
max_image = int(sys.argv[2])

def show(url): print "Descargando:", url

while contador <= max_image:
	if contador < 10:
		url = base_url + "000" + str(contador) + ".jpg"
		urllib.urlretrieve(url, str(contador))
		show(url)
		contador += 1
	elif contador > 9 and contador < 100:
		url = base_url + "00" + str(contador) + ".jpg"
		urllib.urlretrieve(url, str(contador))
		show(url)
		contador += 1
	elif contador > 99:
		url = base_url + "0" + str(contador) + ".jpg"
		urllib.urlretrieve(url, str(contador))
		show(url)
		contador += 1