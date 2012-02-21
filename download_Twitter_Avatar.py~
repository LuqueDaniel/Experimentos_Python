#*-* encoding: utf-8 *-*
#!/usr/bin/env python
from twython import Twython
import sys, urllib

oauth_token = "68772763-JaWRBE88Oi0JsbPZ6IVyoFgLZj3TGUgqtCaohEfNp"
oauth_token_secret = "YCwJfNIhqaLqN0UdjZcpBDpADHxILRziuKpOy7nJOOQ"
consumer_key = "Y07z7hQylwULlW5PzvVNhA"
secret_key = "o47MS9n4MFHBPOGcmV1R7e14LXOvi4BBILADfqOLQ0"

class downTwitterAvatar(object):
	urls = []
	users = []

	def __init__(self):
		self.twitter = Twython(twitter_token=consumer_key,
					   		   twitter_secret=secret_key,
					   		   oauth_token=oauth_token,
					   		   oauth_token_secret=oauth_token_secret)

		self.getUser()
	
	def getUser(self):
		while True:
			self.username = raw_input("Introduzca el username: ").lower()

			if self.username != " " or self.username != "":
				self.getImgURL(self.username)
				self.next = raw_input("¿Obtener otro avatar? (s/n): ").lower()

				if self.next == "s":
					continue
				else:
					break
			else:
				print "Introduzca un nombre de usuario valido!"

	def getImgURL(self,username,size="normal"):
		self.imgURL = self.twitter.getProfileImageUrl(username,size)
		self.users.append(username)
		self.urls.append(self.imgURL)

	def print_url_user(self):
		self.x=0
		for i in self.urls:
			print "Url del avatar de @%s: %s" % (self.users[self.x],i)
			self.x += 1

	def print_url(self):
		for i in self.urls:
			print "Url del avatar: %s" % (i)

	def print_users(self):
		for i in self.users:
			print "@%s"%(i)

	def down_all(self):
		self.x=0
		for url in self.urls:
			urllib.urlretrieve(url, self.users[self.x])
			self.x+=1
	
	""" 
	getImgURL(username,size):
		Funcion que se encarga de obtener las URLs de las imagenes
		sus parametros son username y size

		ATRIBUTOS
		----------------------------------------------------------------------------
		username: El nombre de usuario del que se quiere obtener la URL del avatar

		size: Indica el tamaño del avatar, hay tres posibilidades: 'normal', 'mini'
			  'bigger'. Si no se especifica, por defecto se usara el tamaño 'normal'

	down_all()
		Funcion encargada de realizar la descarga de los avatares.
	"""

img = downTwitterAvatar()
x=0
for i in img.users:
	img.getImgURL(img.users[x],"bigger")
	x+=0

img.print_url_user()
img.down_all()