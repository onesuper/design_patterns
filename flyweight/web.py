#!/usr/bin/python
# Filename: web.py

class Website:
	def __init__(self, name):
		self.name = name
	def Use(self, user):
		print 'This site is about ' + user.name + '\'s ' + self.name

class WebsiteFactory:
	def __init__(self):
		self.flyweights = {}
	def GetWebsiteCategory(self, key):
		if not self.flyweights.has_key(key):
			self.flyweights[key] = Website(key)
		return self.flyweights[key]
	def GetWebsiteCount(self):
		return len(self.flyweights)

