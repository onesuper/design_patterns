#!/usr/bin/python
# Filename: country.py

class Country:
	def __init__(self, mediator):
		self.mediator = mediator

class USA(Country):
	def __init__(self, mediator=0):
		Country.__init__(self, mediator)
	def Declare(self, message):
		self.mediator.Declare(message, self)
	def GetMessage(self, message):
		print 'USE receive:' + message

class Iraq(Country):
	def __init__(self, mediator=0):
		Country.__init__(self, mediator)
	def Declare(self, message):
		self.mediator.Declare(message, self)
	def GetMessage(self, message):
		print 'Iraq receive:' + message
