#!/usr/bin/python
# encoding: utf-8
# Filename: command.py

class BakeMuttonCommand:
	def __init__(self, barbecuer):
		self.receiver = barbecuer
	def ExcuteCommand(self):
		self.receiver.BakeMutton()

class BakeChickenWingCommand:
	def __init__(self, barbecuer):
		self.receiver = barbecuer
	def ExcuteCommand(self):
		self.receiver.BakeChickenWing()


