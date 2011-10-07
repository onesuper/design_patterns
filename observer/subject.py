#!/usr/bin/python
# Filename: subject.py
class Subject:
	def __init___(self):
		self.observers = []
	def Attach(self, observer):
		self.observers.append(observer)
	def Dettach(self, observer):
		self.observers.remove(observer)
	def Notify(self):
		for o in observers:
			o.Update()

