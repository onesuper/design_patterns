#!/usr/bin/python
# Filename: product.py

class Product:
	def __init__(self):
		self.parts = []
	def Add(self, part):
		self.parts.append(part)
	def Show(self):
		print self.parts

class ConcreteBuilder1:
	def __init__(self):
		self.product = Product()
	def BuildPartA(self):
		self.product.Add("partP")
	def BuildPartB(self):
		self.product.Add("partQ")
	def GetResult(self):
		return self.product

class ConcreteBuilder2:
	def __init__(self):
		self.product = Product()
	def BuildPartA(self):
		self.product.Add("PartX")
	def BuildPartB(self):
		self.product.Add("PartY")
	def GetResult(self):
		return self.product
