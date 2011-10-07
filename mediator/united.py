#!/usr/bin/python
# Filename: united.py

import country

class UnitedNation:
	def __init__(self):
		self.member1 = country.USA()
		self.member2 = country.Iraq()
	def Declare(self, message, member):
		if member == self.member1:
			self.member2.GetMessage(message)
		else:
			self.member1.GetMessage(message)
