#!/usr/bin/python
# Filename: proxy.py

class SchoolGirl:
	name = ''

class Pursuit:
	mm = SchoolGirl()
	def __init__(self, mm_name):
		self.mm = mm_name
	def GiveFlowers(self):
		print self.mm.name, 'It is a flower for you'

class Proxy:
	gg = Pursuit('') #there's always a unlucky man behind a luck one
	def __init__(self, mm):
		self.gg = Pursuit(mm)  #create an instance in proxy
	def GiveFlowers(self):
		self.gg.GiveFlowers()  #call the method of gg

		
		
