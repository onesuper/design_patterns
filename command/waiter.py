#!/usr/bin/python
# Filename: waiter.py

class Waiter:
	def __init__(self):
		self.orders = []
	def SetOrder(self, command):
		self.orders.append(command)
		print 'orders add:' + str(command)
	def CancelOrder(self, command):
		self.orders.remove(command)
		print 'orders remove:' + str(command)
	def Notify(self):
		for c in self.orders:
			c.ExcuteCommand()
