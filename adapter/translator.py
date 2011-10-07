#!/usr/bin/python
# Filename: translator.py

import player as p

#now you can direct ForeignCenter to attack
#by calling the tanslator's Attack()
#then he will calling ForeignCenter's JinGong()
class Translator():
	def __init__(self, name):
		self.center = p.ForeignCenter(name)
	def Attack(self):
		self.center.JinGong()
	def Defense(self):
		self.center.FangShou()
