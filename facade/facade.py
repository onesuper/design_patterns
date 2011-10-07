#!/usr/bin/python
# Filename: facade.py
import subSystem as s

class Facade:
	def __init__(self):
		self.one = s.SubSystemOne()
		self.two = s.SubSystemTwo()
		self.three = s.SubSystemThree()
	def MethodA(self):
		print 'Method A'
		self.one.MethodOne()
		self.two.MethodTwo()
	def MethodB(self):
		print 'Method B'
		self.two.MethodTwo()
		self.three.MethodThree()



