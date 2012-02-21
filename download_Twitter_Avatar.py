#*-* encoding: utf-8 *-*
#!/usr/bin/env python
from twython import Twython
import sys, urllib

#Twitter API Key for start Twython
oauth_token = ""
oauth_token_secret = ""
consumer_key = ""
secret_key = ""

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
