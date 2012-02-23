#*-* encoding: utf-8 *-*
#!/usr/bin/env python

class downTwitterAvatar(object):
	urls = []
	users = []

	def __init__(self):
		from twython import Twython
		import sys, urllib

		#Twitter API Key
		self.twitter_token = ""
		self.twitter_secret = ""
		self.twitter = Twython(twitter_token=self.twitter_token, twitter_secret=self.twitter_secret)

		#self.getUser()

	def getImgURL(self,username,size="normal"):
		self.imgURL = self.twitter.getProfileImageUrl(username,size)
		self.users.append(username)
		self.urls.append(self.imgURL)
	
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

#img = downTwitterAvatar()
#
#lista = ["luquedaniel","caballero6x6","richirocko"]
#for i in lista:
#	img.getImgURL(i,"bigger")
#	
#img.print_url_user()
#img.down_all()